#===============================================================================================================

#Aluno : Nicollas Viellas Lee                    #DRE: 123704789

#===============================================================================================================
def questao1(num, ar):
    pares = 0
    cores = list(set(ar))
    for elementos in cores:
        pares += (ar.count(elementos) - (ar.count(elementos)%2))/2

    return pares

#===============================================================================================================

import math
def questao2(AB, BC):
    Teta = math.degrees(math.atan((AB/2)/(BC/2)))
    Teta = round(Teta)
    
    return Teta



#===============================================================================================================

def questao3(string_a, string_b):

    contador = 0
    for a in string_a:
        if a not in string_b:
            contador += 1
    for b in string_b:
        if b not in string_a:
            contador += 1
    return contador

#===============================================================================================================

def questao4(x, n):
    def factorial(n):
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial
    Soma = 0
    Numerador_exp = 0
    Numerador = x
    while Numerador_exp < n:
        Denominador = factorial(Numerador_exp)
        Soma = Soma + ((Numerador)**(Numerador_exp))/Denominador
        Numerador_exp += 1

    return Soma

#===============================================================================================================

def questao5(array):

    lista = []
    numeros = []

    for elementos in array:
        num = int(elementos)
        numeros.append(num)
    lista.append(numeros[0])
    temp = numeros
    lista.append(numeros[temp[0]])
    while -1 not in lista:
        lista.append(numeros[lista[-1]])



    return len(lista)

#===============================================================================================================

def questao6(q):
    suborno = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            return 'caos'
        else:
            for k in range(i - 2, i):
                if k >= 0 and q[k] > q[i]:
                    suborno += 1

    return suborno


#===============================================================================================================

def factorial(n):
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial
def questao7():
    
    num = 0
    numeros = []
    for i in range(0, 50000):
        num += 1
        digitos = []
        Soma = 0
        for d in str(num):
            digitos.append(int(d))

        for l in range(len(digitos)):
            Soma += factorial(digitos[l])
            if Soma == num:
                numeros.append(num)
    return sum(numeros)

