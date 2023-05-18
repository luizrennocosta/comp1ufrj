#import pdbp

def verificar_palindromo(texto):
    """Verifica se um texto é palíndromo.
    
    Args:
        texto(str): texto a ser verificado.
    Returns:   
        is_palindrome(bool): True se o texto é palíndromo, False caso contrário.
    """
    
    # remove espaços e vírgulas para conseguir comparar o texto sem considerar a formação de palavras
    # quando o texto é invertido
    texto = texto.lower().replace(" ", "")
    texto = texto.lower().replace(",", "")
    is_palindrome = (texto == texto[::-1])
    # breakpoint()
    return is_palindrome

def vetor_de_palindromos(lista_textos):
    """Retorna um vetor de booleanos indicando se cada texto da lista é palíndromo.
    
    Args:
        lista_textos(list[str]): lista de textos a serem verificados.
    Returns:
        is_palindrome_array(list[bool]): lista de booleanos indicando se cada texto da lista é palíndromo.
    """
    # return [verificar_palindromo(texto) for texto in lista_textos]
    is_palindrome_array = []
    for texto in lista_textos:
        # breakpoint()
        is_palindrome_array.append(verificar_palindromo(texto))
    return is_palindrome_array
        
def contar_palindromos(textos):
    """Conta quantos textos da lista são palíndromos.
    
    Args:
        textos(list[str]): lista de textos a serem verificados.
    Returns:    
        count(int): quantidade de textos palíndromos contidos na lista.
    """
    count = 0
    for texto in textos:
        if verificar_palindromo(texto):
            # breakpoint()
            count += 2
    return count