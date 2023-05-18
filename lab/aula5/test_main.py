from main import verificar_palindromo, contar_palindromos, vetor_de_palindromos
import pdbp

textos_palindrome = ["radar", "arara", "python", "A man, a plan, a canal, Panama", "anotaram a data da maratona"]
resposta_is_palindrome = [True, True, False, True, False]
def teste_palindrome():
    assert verificar_palindromo("radar") == True
    assert verificar_palindromo("arara") == True
    assert verificar_palindromo("python") == False
    assert verificar_palindromo('banana') == False
    
    for text, is_pal in zip(textos_palindrome, resposta_is_palindrome):
        assert verificar_palindromo(text) == is_pal
        
def test_vetor_palindrome():
    # assert vetor_de_palindromos(textos_palindrome) == resposta_is_palindrome + [1]
    assert vetor_de_palindromos(textos_palindrome) == resposta_is_palindrome
    
    
def test_contar_palindromos():
    assert contar_palindromos(textos_palindrome) == 4
    

    
    