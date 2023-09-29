def questao1(n, ar):
    cores = {}
    pares = 0
    for meia in ar:
        if meia in cores:
            cores[meia] += 1
        else:
            cores[meia] = 1
    for cor, contagem in cores.items():
        pares += contagem // 2
    
    return pares
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
resultado = questao1(n, ar)
print(resultado)


import math

def questao2(AB,BC):
    angulo_rad= math.atan2(AB,BC)
    angulo_deg= math.degrees(angulo_rad)
    angulo_int = round(angulo_deg)

    return angulo_int

angulo1 = questao2(10, 10)
angulo2 = questao2(1, 100)
print (angulo1)
print (angulo2)


def questao3(a, b):
    count_a= {}
    count_b = {}
    for char in a:
        count_a [char] = count_a.get(char, 0) + 1
    for char in b:
        count_b [char] = count_b.get(char, 0) + 1
    total_exclusoes = 0
    for char in 'abcdefghijklmnopqrstuvwxyz':
        freq_a = count_a.get(char, 0)
        freq_b = count_b.get(char, 0)
        total_exclusoes += abs(freq_a - freq_b)
    
    return total_exclusoes
a="cde"
b="abc"
resultado=questao3(a, b)
print(resultado)


def questao4(x, n):
    def conta(n):
        if n == 0:
            return 1
        else:
            return n* conta(n - 1)
    resultado = 0.0
    for i in range(n):
        resultado += (x ** i) / conta(i)
    return resultado
x = 2
n = 10
resultado= questao4(x, n)
print( "%.3f" % resultado)


def questao6(q):
    subornos= 0
    
    for i in range(len(q)-1,-1,-1):
        if q[i]-(i+1)>2:
            print("caos")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                subornos += 1
    print(subornos)
fila1=[1, 2, 3, 5, 4, 6, 7, 8]
fila2=[4, 1, 2, 3]

questao6(fila1)
questao6(fila2)


def questao7():
    def fatorial(n):
        if n==0:
            return 1
        else:
            return n* fatorial(n - 1)
    limite_superior=100000
    numeros_atendendo_condicao=[]
    for num in range(10, limite_superior):
        digitos = [int(digito) for digito in str(num)]
        soma_fatoriais =sum(fatorial(digito) for digito in digitos)
        if soma_fatoriais== num:
            numeros_atendendo_condicao.append(num)
    soma_total=sum(numeros_atendendo_condicao)
    return soma_total
resultado=questao7()
print(resultado)