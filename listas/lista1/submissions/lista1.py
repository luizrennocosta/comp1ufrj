#Exercício 1

def contar_pares_de_meias(n, ar):
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

quantidade_de_pares = contar_pares_de_meias(n, meias)
#print("O número de pares de meias na pilha é:", quantidade_de_pares)


#Exercício 2

import math

AB = 100
BC = 250

angulo_radianos = math.atan2(AB, BC)

angulo_graus = math.degrees(angulo_radianos)

angulo_arredondado = round(angulo_graus)

#print("O ângulo ∠MBC é:", angulo_arredondado, "graus")


#Exercício 3

def minExclusoesParaAnagramas(a, b):
    count_a = [0] * 26  # 26 letras do alfabeto
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
result = minExclusoesParaAnagramas(a, b)
#print("Número mínimo de exclusões:", result)  # Deve imprimir 0, pois são anagramas


#Exercício 4

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def calculate_exponential(x, n):
    result = 0.0
    for i in range(n):
        term = (x ** i) / factorial(i)
        result += term
    return result

x = 2  # Número para calcular a exponencial natural
n = 1000  # Um grande número de termos tendendo ao infinito

exponential_result = calculate_exponential(x, n)
#print(f"Aproximação da exponencial natural de {x} com {n} termos é aproximadamente: {exponential_result}")


#Exercício 5

def len_of_linked_list(A):
    if not A:
        return 0  # Se a lista não tiver nada, o comprimento é 0

    length = 0
    current_index = 0

    while A[current_index] != -1:
        length += 1
        current_index = A[current_index]  

    length += 1

    return length

# Exemplo de uso:
A = [1, 4, -1, 3, 2]
result = len_of_linked_list(A)
#print("O comprimento da lista construída a partir de A é:", result)


#Exercício 6

def minimo_de_subornos(q):
    subornos = 0  # Inicializa o número de subornos como 0

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("caos")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                subornos += 1

    #print(subosnos)

# Função principal para lidar com os casos de teste
def main():
    t = int(input())  # Número de casos de teste

    for _ in range(t):
        n = int(input())  # Número de pessoas na fila
        q = list(map(int, input().split()))  # Estado final da fila
        minimo_de_subornos(q)  # Chama a função para determinar os subornos

if __name__ == "__main__":
    main()

    #print(minimo_de_subornos)