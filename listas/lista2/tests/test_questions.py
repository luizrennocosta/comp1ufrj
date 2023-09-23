import pytest
import math
from answers import questao1, questao2, questao3, questao4, questao5  # Altere 'nome_do_arquivo' para o nome correto do arquivo onde as funções estão.
import pickle
import os
import pathlib

def load_input_output(file):
    file = os.path.join(pathlib.Path(__file__).parent.absolute(), file)
    with open(file, "rb") as f:
        q_dict = pickle.load(f)
    return q_dict

exemplos_gerados = load_input_output('questoes_pickle')

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

# Testes para a questão1
@pytest.mark.parametrize("entrada, saida_esperada", [(dados['input'], dados['output']) for dados in exemplos_gerados['questao1']])
def test_questao1(entrada, saida_esperada):
    assert verificar_iguais(questao1(*entrada), saida_esperada)

# Testes para a questão2
@pytest.mark.parametrize("entrada, saida_esperada", [(dados['input'], dados['output']) for dados in exemplos_gerados['questao2']])
def test_questao2(entrada, saida_esperada):
    assert verificar_iguais(questao2(entrada), saida_esperada)

# Testes para a questão3
@pytest.mark.parametrize("entrada, saida_esperada", [(dados['input'], dados['output']) for dados in exemplos_gerados['questao3']])
def test_questao3(entrada, saida_esperada):
    assert verificar_iguais(questao3(entrada), saida_esperada)

# Testes para a questão4
@pytest.mark.parametrize("entrada, saida_esperada", [(dados['input'], dados['output']) for dados in exemplos_gerados['questao4']])
def test_questao4(entrada, saida_esperada):
    assert verificar_iguais(questao4(entrada), saida_esperada)

# Testes para a questão5
@pytest.mark.parametrize("entrada, saida_esperada", [(dados['input'], dados['output']) for dados in exemplos_gerados['questao5']])
def test_questao5(entrada, saida_esperada):
    entrada = os.path.join(pathlib.Path(__file__).parent.absolute(), entrada)
    assert verificar_iguais(questao5(entrada), saida_esperada)
