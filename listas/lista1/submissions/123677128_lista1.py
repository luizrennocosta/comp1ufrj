#Exercício 1

def questao1(n, ar):
    contagem_de_cores = {}
    
    pares = 0
    
    for cor in ar:
        if cor in contagem_de_cores:
            contagem_de_cores[cor] += 1
        else:
            contagem_de_cores[cor] = 1
    
    for cor, quantidade in contagem_de_cores.items():
        pares += quantidade // 2
    
    return pares

n = 15
meias = [1, 3, 3, 1, 1, 2, 5, 1, 3, 4, 5, 4, 6, 2, 3]

quantidade_de_pares = questao1(n, meias)
#print("O número de pares de meias na pilha é:", quantidade_de_pares)


#Exercício 2

import math

def questao2(AB, BC):
    tangente_MBC = AB / BC

    angulo_radianos = math.atan(tangente_MBC)

    angulo_graus = math.degrees(angulo_radianos)

    angulo_arredondado = round(angulo_graus)

    return angulo_arredondado

AB = 100
BC = 200

angulo_MBC = questao2(AB, BC)
#print("O ângulo ∠MBC é:", angulo_MBC, "graus")



#Exercício 3

def questao3(a, b):
    count_a = [0] * 26  
    count_b = [0] * 26
    
    for char in a:
        count_a[ord(char) - ord('a')] += 1

    for char in b:
        count_b[ord(char) - ord('a')] += 1

    total_exclusions = 0
    for i in range(26):
        total_exclusions += abs(count_a[i] - count_b[i])

    return total_exclusions

# Exemplo de uso:
a = "counterstrike"
b = "overwatch"
result = questao3(a, b)
#print("Número mínimo de exclusões:", result) 

#Exercício 4

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def questao4(x, n):
    result = 0.0
    for i in range(n):
        term = (x ** i) / factorial(i)
        result += term
    return result

x = 2 
n = 1000 

exponential_result = questao4(x, n)
#print(f"Aproximação da exponencial natural de {x} com {n} termos é aproximadamente: {exponential_result}")




#Exercício 5


def questao5(A):
    N = len(A)
    visitado = [False] * N 
    comprimento = 0  

    index = 0

    while index != -1:
        if visitado[index]:
            break

        visitado[index] = True  
        index = A[index]  
        comprimento += 1 

    return comprimento
# Exemplo de uso:
A = [0, 5, -1, 3, -2]
resultado = questao5(A)
#print(resultado)






#Exercício 7

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def questao7(numero):
    return sum(fatorial(int(digito)) for digito in str(numero))

    limite_superior = 50000  

    numeros_curiosos = []
    for i in range(1, limite_superior):
        if i == questao7(i):
            numeros_curiosos.append(i)


soma_total = sum(numeros_curiosos)

#print("Soma total dos números curiosos:", soma_total)

