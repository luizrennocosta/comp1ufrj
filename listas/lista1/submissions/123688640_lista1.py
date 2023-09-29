print("\033c")
import math

#Questão 1
def questao1(n, ar):
    cores = [0] * 101
    for cor in ar:
        cores[cor] += 1
    pares = 0
    for cont in cores:
        pares += cont // 2

    print(pares)
    return pares

#Questão 2
#Biblioteca Math foi importada no começo do código.
def questão2(ab, bc):
    tangente = ab/bc
    angulo = math.atan(tangente)
    graus = round(math.degrees(angulo))
    
    print(graus)
    return graus

#Questão 3
def questao3(a, b):
    lista_a = [0] * 26
    lista_b = [0] * 26
    contador = ord('a')
    for letra in a:
        lista_a[ord(letra) - contador] += 1 
    for letra in b:
        lista_b[ord(letra) - contador] += 1
    exclusoes = 0
    for i in range(26):
        exclusoes += abs(lista_a[i] - lista_b[i])
    
    print(exclusoes)
    return exclusoes

#Questão 4
#"n" só pode assumir valores inteiros.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def questão4(x, n):
    resultado = 0
    for valor in range(n):
        calculo = (x**valor) / factorial(valor)
        resultado += calculo

    print(resultado)
    return resultado

#Questão 5
def questão5(ar):
    comprimento=1 
    i=0
    while ar[i]!=-1:
        comprimento+=1
        i=ar[i]

    print(comprimento)
    return comprimento

#Questão 6
def questao6(q):
    subornos = 0
    for posição_atual, posição_original in enumerate(q):
        if posição_original - (posição_atual + 1) > 2:
            return "caos"
        for checagem in range(max(0, posição_original - 2), posição_atual):
            if q[checagem] > posição_original:
                subornos += 1
    
    print(subornos)
    return str(subornos)

#Questão 7
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def questao7():
    numeros_curiosos = []
    for numero in range(1, 50000):
        soma_fatoriais = sum(factorial(int(digito)) for digito in str(numero))
        if soma_fatoriais == numero:
            numeros_curiosos.append(numero)
    return sum(numeros_curiosos)