import csv
import pytest
import os
import importlib.util
import pandas as pd
import xml.etree.ElementTree as ET
import sys
import re
import numpy as np

import gspread
import pandas as pd
import re
import dotenv
import argparse
from download_student_submissions import download_student_submissions

dotenv.load_dotenv()
# Setup gspread with Google Sheets API credentials
gc = gspread.service_account(filename=os.getenv('GOOGLE_CRED_FILE'))

bonus_questions = {1: [7], 2: [6]}

def parse_test_results(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    results = {}

    # Iterate over each testcase within testsuite
    for testcase in root.find('./testsuite').findall('testcase'):
        test_name = testcase.get('name')

        # Extract the question and example number from the test name
        # For example: from "test_questao_1[example0]" to "questao_1" and "example0"
        questao = test_name.split('[')[0].split('test_')[1]
        example = test_name.split('[')[1].split(']')[0]

        if not list(testcase):
            results[(questao, example)] = ('Passed', None)
        else:
            error_msg = testcase.find('failure').text
            results[(questao, example)] = ('Failed', error_msg)

    return results

def import_student_module(student_id, module_path):
    module_name = f"student_module_{student_id}"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_tests_for_student(local_folder, student_module):
    
    for func_name, func in student_module.__dict__.items():
        if callable(func) and not func_name.startswith("__"):
            try:
                delattr(sys.modules['tests.test_questions'], func_name)
            except:
                continue
    # We dynamically insert the student's functions into the test module namespace
    for func_name, func in student_module.__dict__.items():
        if callable(func) and not func_name.startswith("__"):
            setattr(sys.modules['tests.test_questions'], func_name, func)

    results_dct = {}
    # Run the tests for the current student's functions
    # pytest.main(['tests/test_questions.py', '--quiet'], plugins=[pytest_harvest.ResultsBagPlugin(results_dct)])
    
    pytest.main([f'{local_folder}/tests/test_questions.py', '--quiet', '--junitxml=results.xml'])
   
    for func_name, func in student_module.__dict__.items():
        if callable(func):
            delattr(sys.modules['tests.test_questions'], func_name)

def upload_dataframe(df, start_cell = None):
    # Open the Google Spreadsheet using its name (or URL or key)
    spreadsheet = gc.open_by_key(os.getenv('GRADES_SHEETS_ID'))

    # Select the specific sheet you want to upload to
    for lista in df.list.unique():
        worksheet = spreadsheet.worksheet(f"Lista {lista}")
        headers = df.drop(columns='list').columns.tolist()
        if start_cell is None:
        
            # Clear existing data in the sheet (optional, but useful if you're re-uploading data)
            worksheet.clear()
            
            # Convert the DataFrame to a list of lists and update the sheet
            rows = df[df['list'] == lista].drop(columns='list').values.tolist()
            
            worksheet.insert_rows([headers]+rows, row=2, value_input_option='USER_ENTERED')
        else:
                        
            col_start = gspread.utils.a1_to_rowcol(start_cell)[1]
            row_start = gspread.utils.a1_to_rowcol(start_cell)[0]
            
            # Compute the end cell based on DataFrame's dimensions
            row_end = row_start + len(df) 
            col_end = col_start + len(df.columns) - 1
            
            end_cell = gspread.utils.rowcol_to_a1(row_end, col_end)
            
            # Define the target range
            cell_range = f"{start_cell}:{end_cell}"
            
            # Update the Google Sheet with DataFrame data
            worksheet.update(cell_range, [headers] + df.drop(columns='list').values.tolist(), value_input_option='USER_ENTERED')

def calculate_consolidated_grade(df, bonus_questions):
    current_list = df['list'].values[0]
    n_questions = df.shape[0]
    b_question = bonus_questions.get(current_list, [])
    
    df['nota'] = df['status'] / df['n_tests']
    
    if len(b_question) > 0:
        mask = df['question'].isin(b_question)
        normal_questions = df[~mask]
        bonus_questions = df[mask]
        
        nota = normal_questions['nota'].mean().round(2) + (bonus_questions['nota'].sum()/10).round(2)
    else:         
        nota = df['nota'].mean().round(2)
        
    return pd.Series({'nota': nota})
def grade_students(local_folder):
    # Creating a list to store the rows for our DataFrame
    rows = []
    pattern = r'E[\s]*([a-zA-Z]*Error:.*)'

    for student_file in os.listdir(f'{local_folder}/submissions'):
        if student_file.endswith('.py'):
            student_id = os.path.splitext(student_file.lower())[0]
            try:
                student_id, list_id = student_id.split('_')
            except:
                print(f"Couldn't parse student ID and list ID from filename {student_file}")
                continue
            try:
                list_id = int(list_id.replace('lista', ''))
            except:
                print(f"Couldn't parse list id from filename {student_file}")
                continue
            student_module_path = os.path.join(f'{local_folder}/submissions', student_file)
            
            try:
                student_module = import_student_module(student_id, student_module_path)
            except Exception as e:
                print(f'file for student {student_file} with syntax errors')
                print(e)
                row_data = {'DRE': student_id, 'list': list_id, 'n_tests': 1,
                            'status': 0, 'question': 0, 'error_message': f'Syntax error: {e}'}
                rows.append(row_data.copy())
                continue
            run_tests_for_student(local_folder, student_module)
            
            test_results = parse_test_results('results.xml')
            
            bonus_questions_from_list = bonus_questions.get(list_id, [])
            # Create a dictionary to represent the row of data
            row_data = {'DRE': student_id, 'list': list_id, 'n_tests': 1}
            for (test_name, example_name), (status, message) in test_results.items():
                found_errors = []
                if status == 'Failed':
                    try:
                        found_errors = re.findall(pattern, message)
                    except Exception as e:
                        print(f'something went wrong on findall')
                        print(e)
                        print(f'message: {message}')
                        found_errors = -1
                # Assuming a naming convention for tests as mentioned earlier
                row_data['status'] = 10 if status == 'Passed' else 0
                row_data['question'] = int(re.findall(r'\d+', test_name)[0])
                if len(found_errors) > 0:
                    row_data['error_message'] = (f'[{example_name}]-' + found_errors[0] + '; ') if status == 'Failed' else None
                elif found_errors == -1:
                    print(f'Unknown error found for {student_file}, needs further checking')
                    row_data['error_message'] = (f'[{example_name}]-' + '; ') if status == 'Failed' else None
                else:
                    row_data['error_message'] = None
                rows.append(row_data.copy())
    
    # Convert the list of rows to a DataFrame
    now_time = pd.Timestamp.now()
    df = pd.DataFrame(rows)
    df = df.groupby(by=['DRE', 'question']).agg({'list': 'first', 'status': 'sum', 'error_message': 'sum', 'n_tests': 'sum'}).reset_index()
    df['updated_at'] = now_time
    df['updated_at'] = df['updated_at'].astype(str)
    
    # Writing the DataFrame to a CSV file
    df.to_csv('grades.csv', index=False)
    upload_dataframe(df)
    

    agg_grade_df = df.groupby(by=['DRE', 'list']).apply(calculate_consolidated_grade, bonus_questions).reset_index()
    agg_grade_df['updated_at'] = now_time
    agg_grade_df['updated_at'] = agg_grade_df['updated_at'].astype(str)
    print(agg_grade_df)

    upload_dataframe(agg_grade_df, 'I2')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download student submissions from Google Drive')
    parser.add_argument('--list', type=str, default='venv', help='List name')
    args = parser.parse_args()
    
    g_drive_id_env = f'{args.list.upper()}_DRIVE_ID'
    local_folder = f'{args.list}'
    sys.path.append(os.getcwd())
    sys.path.append(os.path.join(os.getcwd(), local_folder))
    sys.path.append(os.path.join(os.getcwd(), os.path.join(local_folder, 'tests')))
    import tests.test_questions
    
    folder_id = os.getenv(g_drive_id_env)
    download_student_submissions(folder_id, local_folder)
    grade_students(local_folder)
