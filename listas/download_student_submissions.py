import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import argparse

def download_student_submissions(g_drive_folder_id, local_folder):
    """
    Download student submissions from Google Drive
    """
    
     # Load the service account credentials
    creds = Credentials.from_service_account_file(os.getenv('GOOGLE_CRED_FILE'), 
                                                scopes=['https://www.googleapis.com/auth/drive.readonly'])

    drive_service = build('drive', 'v3', credentials=creds)

    # List files in the Google Drive folder
    
    results = drive_service.files().list(q=f"'{g_drive_folder_id}' in parents",
                                        fields="files(id, name, modifiedTime)").execute()
    items = results.get('files', [])

    # Filter out the most recent files in case of duplicates
    filtered_files = {}
    for item in items:
        if item['name'] in filtered_files:
            if item['modifiedTime'] > filtered_files[item['name']]['modifiedTime']:
                filtered_files[item['name']] = item
        else:
            filtered_files[item['name']] = item

    # Download the files
    for filename, file_info in filtered_files.items():
        request = drive_service.files().get_media(fileId=file_info['id'])
        try:
            with open(f'{local_folder}/submissions/{filename}', 'wb') as f:
                downloader = MediaIoBaseDownload(f, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(f"Downloaded {int(status.progress() * 100)}% of {filename}")
        except:
            print(f'file {filename} failed to download')
    print("All files downloaded!")
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download student submissions from Google Drive')
    parser.add_argument('--list', type=str, default='', help='List name')
    args = parser.parse_args()
    
    g_drive_id_env = f'{parser.list.upper()}_DRIVE_ID'
    local_folder = f'{parser.list}'
    
    folder_id = os.getenv(g_drive_id_env)
    
    download_student_submissions(folder_id, local_folder)
   
