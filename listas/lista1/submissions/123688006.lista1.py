# ****** Questão 1 ******
def questao1(ar):
    cores = [0] * 101

    for cor in ar:
        cores[cor] += 1

    pares = 0
    for cont in cores:
        pares += cont // 2

    print(pares)
    return pares


# ****** Questão 2 ******
import math
def questao2(ab, bc):
    tangente = ab / bc
    angulo = math.atan(tangente)
    graus = round(math.degrees(angulo))

    print(graus)
    return graus


# ****** Questão 3 ******
def questao3(a, b):
    repet_a = {}
    repet_b = {}

    for letra in a:
        repet_a[letra] = repet_a.get(letra, 0) + 1
    for letra in b:
        repet_b[letra] = repet_b.get(letra, 0) + 1
    exclusoes = 0

    for letra, freq in repet_a.items():
        if letra in repet_b:
            exclusoes += abs(freq - repet_b[letra])
        else:
            exclusoes += freq

    for letra, freq in repet_b.items():
        if letra not in repet_a:
            exclusoes += freq

    print(exclusoes)
    return exclusoes


# ****** Questão 4 ******
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def questao4(x, n):
    resultado = 0
    for valor in range(n):
        calculo = (x ** valor) / factorial(valor)
        resultado += calculo

    print(resultado)
    return resultado
# ****** Questão 5 ******
def questao5(a):
    comprimento = 0
    index = 0

    while index != -1:
        comprimento += 1
        index = a[index]

    return comprimento

# ****** Questão 6 ******
def questao6(q):
    subornos = 0
    n = len(q)

    for i in range(n - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("caos")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                subornos += 1

    print(subornos)


t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))

    questao6(q)


#****** Questão 7 ******
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def questao7():
    soma = 0
    for valor in range(3, 50000):
        if valor == sum(factorial(int(d)) for d in str(valor)):
            soma += valor

    return soma

resultado = questao7()
print(resultado)
