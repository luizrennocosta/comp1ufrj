#1º QUESTÃO
def questao1(n, ar):

    nº_cores = [0] * 101

    for cor in ar:
        nº_cores[cor] += 1

    pares = 0

    for c in nº_cores:
        pares += c // 2

    return pares

#2ª QUESTÃO
import math
def questao2(AB,BC):
    tg = math.atan2(AB, BC)
    graus = math.degrees(tg)
    arredondado = round(graus)

    return arredondado

#3ª QUESTÃO
def questao3(a,b):
    cont_a = [0] * 26
    cont_b = [0] * 26

    for char in a:
        cont_a[ord(char) - ord('a')] += 1
    for char in b:
        cont_b[ord(char) - ord('a')] += 1
        exclusoes = 0
        for i in range(26):
            exclusoes = abs(cont_a[i] - cont_b[i])

        return exclusoes


#4ª QUESTÃO
def  factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n- 1)

def calcular_exponencial(x, n):
    resultado = 0.0

    for i in range(n):
        termo = (x ** i) /factorial(i)
        resultado += termo

    return resultado

#5ª QUESTÃO
def questao5(A):
    if not A:
        return 0

    comprimento = 0
    i = 0

    while i!= -1:
        i = A[i]

    return comprimento


#6ª QUESTÃO
def subornos(q):
    subornos = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("caos")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
               subornos += 1

    print(subornos)



#7ª QUESTÃO
def questao7(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    soma_total = 0

    for num in range(10, 100000):
        digitos = [int(digit) for digit in str(num)]
        soma_fatoriais = sum(fatorial(d) for d in digitos)

        if num == soma_fatoriais:
            soma_total += num

    print(soma_total)
