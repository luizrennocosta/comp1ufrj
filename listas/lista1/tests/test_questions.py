import pickle
import pytest
import os
import pathlib
import math

def load_input_output(file):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    with open(file, "rb") as f:
        q_dict = pickle.load(f)
    return q_dict

questoes = load_input_output('questoes_pickle')

def verificar_iguais(resultado, esperado):
    # Verifica se dois valores ou duas estruturas de dados são aproximadamente iguais (para floats) ou exatamente iguais (para outros tipos).
    if isinstance(resultado, float) and isinstance(esperado, float):
        return math.isclose(resultado, esperado, rel_tol=1e-5)
    elif isinstance(resultado, list) and isinstance(esperado, list):
        return all(verificar_iguais(r, e) for r, e in zip(resultado, esperado))
    elif isinstance(resultado, dict) and isinstance(esperado, dict):
        return all(verificar_iguais(resultado[k], esperado[k]) for k in resultado)
    else:
        return resultado == esperado


@pytest.mark.parametrize('example', questoes['questao1'])
def test_questao1(example):
    expected = example['output']
    actual = questao1(example['input'][0], example['input'][1])
    assert actual == expected, "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, actual)        

    
@pytest.mark.parametrize('example', questoes['questao2'])
def test_questao2(example):
    expected = example['output']
    actual = questao2(example['input'][0], example['input'][1])
    assert actual == expected, "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, actual)        

@pytest.mark.parametrize('example', questoes['questao3'])
def test_questao3(example):
    expected = example['output']
    actual = questao3(example['input'][0], example['input'][1])
    assert actual == expected, "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, actual)        

    
@pytest.mark.parametrize('example', questoes['questao4'])
def test_questao4(example):
    expected = example['output']
    actual = questao4(example['input'][0], example['input'][1])
    
    assert verificar_iguais(actual, expected)
   # assert actual == expected, "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, actual)        


@pytest.mark.parametrize('example', questoes['questao5'])
def test_questao5(example):
    expected = example['output']
    actual = questao5(example['input'])
    assert actual == expected, "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, actual)
    
@pytest.mark.parametrize('example', questoes['questao6'])
def test_questao6(example, capsys):
    expected = example['output']
    questao6(example['input'])
    captured = capsys.readouterr()
    calculated = captured.out
    assert calculated.strip() == str(expected), "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, calculated)

questoes['questao7'] = [{'input': [], 'output': 40733}]
@pytest.mark.parametrize('example', questoes['questao7'])
def test_questao7(example):
    expected = 40733
    actual = questao7()
    assert actual == expected, "Resultado esperado:{0}, Resultado calculado:{1}".format(expected, actual)
    
