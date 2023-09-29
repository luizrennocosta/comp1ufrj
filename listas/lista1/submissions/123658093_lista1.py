def questao1(n, ar):
    contagem_cores = [0] * 101 
    num = 0
    
    for meia in ar:
        contagem_cores[meia] = contagem_cores[meia] + 1
        if contagem_cores[meia] % 2 == 0:
            num = num + 1

    return num


import math

def questao2(AB, BC):
    angulo_MBC_radianos = math.atan2(AB, BC)
    angulo_MBC_graus = math.degrees(angulo_MBC_radianos)

    return int(round(angulo_MBC_graus))


def questao3(a, b):
    frequencia_a = {}

    for letra in a:
        if letra in frequencia_a:
            frequencia_a[letra] = frequencia_a[letra] + 1
        else:
            frequencia_a[letra] = 1

    total_exclusoes = 0

    for letra in b:
        if letra in frequencia_a and frequencia_a[letra] > 0:
            frequencia_a[letra] = frequencia_a[letra] - 1
        else:
            total_exclusoes = total_exclusoes + 1

    total_exclusoes = total_exclusoes + sum(frequencia_a.values())

    return total_exclusoes


def factorial(n):
    if n == 0:
        return 1
    result = 1
    num = 1
    while contador <= n:
        result = result * contador
        num = num + 1
    return result

def questao4(x, n):
    result = 0.0
    num = 0
    while contador < n:
        result = result + (x ** num) / factorial(num)
        num = num + 1
    return result


def questao5(A):
    N = len(A)
    if N == 0:
        return 0

    comprimento = 1
    atual = A[0]

    while atual != -1:
        atual = A[atual]
        comprimento = comprimento + 1

    return comprimento

def questao6(casos):
    for fila in casos:
        subornos = 0
        i = 0

        while i < len(fila):
            if fila[i] - (i + 1) > 2:
                print("caos")
                return

            i_comparacao = i - 2 if i >= 2 else 0

            while i_comparacao < i:
                if fila[i_comparacao] > fila[i]:
                    subornos = subornos + 1
                i_comparacao = i_comparacao + 1
            
            i = i + 1

        print(subornos)



def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def questao7():
    numeros_curiosos = []
    limite_superior = 7 * fatorial(9)

    num = 10
    while num <= limite_superior:
        soma_fatoriais_digitos = sum(fatorial(int(digito)) for digito in str(num))
        if soma_fatoriais_digitos == num:
            numeros_curiosos.append(num)
        num += 1

    return numeros_curiosos






