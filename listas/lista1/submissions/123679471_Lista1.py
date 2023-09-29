# -*- coding: utf-8 -*-
def questao1(n, coresmeias):
    paresrepetidos = 0
    idx = 0
    while idx < len(coresmeias):
        for x in range(idx + 1, len(coresmeias)):
            if coresmeias[idx] == coresmeias[x]:
                paresrepetidos += 1
                del coresmeias[x]
                break
        idx += 1
    return paresrepetidos

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = questao1(n, ar)
print(result)  # This should print 3

import math
def questao2(AB, BC):
    if AB <= 1000 and BC <= 1000:
        arcotangente = math.degrees(math.atan(AB/BC))
        angulo = round(arcotangente)
        return angulo
    else:
        return print("Números acima de 1000 para algum ou para os dois lados")

def questao3(stringA, stringB):
    stringA = stringA.lower()
    stringB = stringB.lower()
    
    listaA = list(stringA)
    listaB = list(stringB)
    exclusoes = 0
    
    ListaA2 = []
    ListaB2 = []

    for x in listaA:
        if x not in listaB:
            exclusoes += 1
        else:
            ocorrencialetraA = listaA.count(x)
            ocorrencialetraB = listaB.count(x)
            if ocorrencialetraA > ocorrencialetraB:
                exclusoes += (ocorrencialetraA - ocorrencialetraB)
            elif ocorrencialetraB > ocorrencialetraA:
                exclusoes += (ocorrencialetraB - ocorrencialetraA)
            ListaA2.append(x)
            ListaB2.append(x)
            
    for x in listaB:
        if x not in listaA:
            exclusoes += 1

    return exclusoes

def questao4(x, n):
    FuncaoExponencial = 0
    for i in range(n):
        FuncaoExponencial += (x ** i) / factorial(i)
    return print(FuncaoExponencial)
def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1
    
def questao5(A):
    Indice = A[0]
    Tamanho = 1
    while Indice != -1:
        Tamanho += 1
        Indice = A[Indice]

    return Tamanho

def questao6(q):
    contadorsubornos = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("caos")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                contadorsubornos += 1
    print(contadorsubornos)
    
def factorialsete(n):
    if n != 0:
        return n * factorialsete(n - 1)
    else:
        return 1

def SomaAlgarismosFatorial(numero):
    soma = 0
    for d in str(numero):
        soma += factorial(int(d))
    return soma

def questao7():
    maximo = 50000
    soma = 0

    for num in range(0, maximo):
        if num == SomaAlgarismosFatorial(num):
            soma += num

    return soma