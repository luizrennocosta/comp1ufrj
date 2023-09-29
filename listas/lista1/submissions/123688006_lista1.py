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
    for posicao_atual, posicao_original in enumerate(q):
        if posicao_original - (posicao_atual + 1) > 2:
            return "caos"
        for checagem in range(max(0, posicao_original - 2), posicao_atual):
            if q[checagem] > posicao_original:
                subornos += 1

    print(subornos)
    return str(subornos)


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
