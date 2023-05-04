def is_prime(number):
    """Verifica se um número é primo e retorna True ou False"""
    # Divisor começa em 2, pois 1 é divisor de todos os números
    divisor = 2
    is_prime = True
    # Itera todos os possíveis divisores do número até ele mesmo
    while divisor < number:
        if number % divisor == 0:
            # Se o número for divisível por algum número (além dele e 1), ele não é primo
            is_prime=False
        divisor += 1
    print(f"o número {number} é primo? {is_prime}")
    return is_prime        


def todos_divisores_e_maior_comum(numero_menor, numero_maior):
    """Retorna o maior divisor comum entre dois números"""
    divisor = 1
    maior_denominador_comum = 1
    # Itera todos os possíveis divisores do número até ele mesmo
    while divisor <= numero_maior:
        if numero_maior%divisor == 0 and numero_menor%divisor == 0:
            # Se o divisor for comum entre os dois números, ele é o maior divisor comum
            print(f"um divisor comum entre {numero_menor} e {numero_maior} é: {divisor}")
            maior_denominador_comum = divisor
        divisor += 1
    return maior_denominador_comum


def verifica_primo_e_divisores(a,b):
    """Verifica se a e b são primos e retorna o maior divisor comum entre eles"""
    a_primo = is_prime(a)
    b_primo = is_prime(b)
    
    # Verifica qual é o maior número e chama a função que calcula o maior divisor comum
    # isso é necessário pois a função de divisor assume que o primeiro número é menor
    if b > a:
        maior_divisor = todos_divisores_e_maior_comum(a, b)
    else:
        maior_divisor = todos_divisores_e_maior_comum(b, a)
        
    return a_primo, b_primo, maior_divisor


if __name__ == '__main__':
    print(verifica_primo_e_divisores(2, 2))