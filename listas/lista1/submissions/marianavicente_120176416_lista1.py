def questao1(n, ar):
#saber quantos pares de meia da mesma cor tem 
       cores = {}
       for cor in ar:
           if cor in cores:
               cores[cor] += 1
           else:
               cores[cor] = 1
       pares = 0
       for contagem in cores.values():
           pares += contagem // 2
       return pares

print (questao1(7, [29, 29, 21, 37, 21, 5, 21]))
print (questao1(10, [10, 42, 46, 46, 6, 42, 18, 18, 42, 18])) 
print (questao1(11, [20, 35, 15, 15, 25, 40, 30, 20, 40, 45, 20])) 
print (questao1(7, [36, 36, 15, 22, 36, 43, 36])) 
print (questao1(15, [28, 37, 28, 28, 37, 37, 37, 28, 19, 37, 37, 37, 37, 28, 28]))
print (questao1(5, [31, 37, 22, 34, 31])) 
print (questao1(8, [24, 14, 4, 24, 24, 14, 14, 24]))
print (questao1(6, [34, 16, 25, 34, 25, 34])) 
print (questao1(13, [20, 28, 20, 28, 44, 44, 44, 20, 20, 20, 20, 28, 36])) 
print (questao1(11, [13, 13, 13, 13, 22, 13, 13, 13, 13, 22, 22]))


import math

def questao2(AB, BC):
    angulo = round(math.degrees(math.atan(AB / BC)))
    return angulo
print (questao2(52, 34))
print (questao2(91, 13))
print (questao2(25, 30))
print (questao2(7, 50))
print (questao2(35, 1))
print (questao2(35, 39))
print (questao2(5, 4))
print (questao2(72, 38))
print (questao2(30, 52))
print (questao2(2, 84))



def questao3(a, b):
#Saber quantidade mínima de números a se excluídos para a e b
#se um anagrama(te as mesmas letras ’’’
    string1 = [0] * 26
    string2 = [0] * 26
    for criptografia in range(len(a)):
        string1[ord(a[criptografia]) - ord('a')] += 1
    for criptografia in range(len(b)):
        string2[ord(b[criptografia]) - ord('a')] += 1
    anagrama = 0
    for i in range(26):
         anagrama+= abs(string1[i] - string2[i])
    return anagrama
print (questao3('cgha','idge'))
print (questao3('jagii','bggad'))
print (questao3('bdecbifcg','eifgb')) 
print (questao3('fcde','iaaeabba'))
print (questao3('fibj','bjhdi'))
print (questao3('gedg','jchhdaaffb'))
print (questao3('hde','ajifafjhga'))
print (questao3('egbddg','digj')) 
print (questao3('dbfgbb','adccgehaj'))
print (questao3('efgie','aeedbbcc'))


def questao4(x, n):
    def factorial (n):
#funcao que recebe o x por argumento, a quantidade de elementos n
#e retorna o valor da sua exponencial
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    soma = 1.0

    for exponencial in range(1, n):
        termo= (x ** exponencial ) / factorial(exponencial)
        soma += termo

    return soma

print(questao4(1.47,7))
print(questao4(1.3,1))
print(questao4(3.64,4))
print(questao4(4.28,3))
print(questao4(0.26,7))
print(questao4(0.46,6))
print(questao4(0.6,10))
print(questao4(2.36,4))
print(questao4(3.87,9))
print(questao4(1.19,1))


def questao5(A):
#Escreva uma funcao que, dado um array nao vazio A consistindo de N inteiros, retorne o com- primento da lista construida
    comprimento = 1
    indice = 0
    while A[indice] != -1:
         comprimento += 1
         indice = A[indice]

    return comprimento
print(questao5([4,2,9,5,11,7,8,10,3,6,1,-1]))
print(questao5([5,2,6,4,-1,9,8,3,1,7]))
print(questao5([3,4,-1,1,2]))
print(questao5([3,1,5,6,-1,8,2,4,7]))
print(questao5([7,9,11,2,6,10,3,8,5,4,-1,1]))
print(questao5([3,11,13,4,6,12,2,8,10,9,-1,1,7,5]))
print(questao5([4,1,3,2,-1]))
print(questao5([1,2,3,5,4,-1]))
print(questao5([6,-1,4,5,8,9,2,3,1,7]))
print(questao5([3,1,-1,4,2]))


def questao6(q):
#Determine o numero ḿınimo de subornos que ocorreu para chegar a uma determinada ordem na fila
    suborno = 0
    for  pos in range(len(q) - 1, -1, -1):
         if q[pos] - (pos+ 1) > 2:
            print("caos")
            return
         for fila in range(max(0, q[pos] - 2), pos):
            if q[fila] > q[pos]:
                  suborno += 1
    print(suborno)

print (questao6([1, 2, 4, 3, 6, 5, 7, 8, 12, 9, 10, 11, 14, 13, 15, 17, 16, 18, 21, 19, 20, 22, 23, 25, 24]))
print (questao6([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 19, 17, 18, 22, 20, 21, 25, 23, 24, 27, 26]))
print (questao6([1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 15, 14, 17, 16, 18, 19, 21, 20, 22, 23, 24]))
print (questao6([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 12, 11, 13, 14, 15, 16, 17, 20, 18, 19, 23, 21, 22, 24, 25]))
print (questao6([1, 2, 4, 3, 5, 6, 8, 7, 10, 9, 13, 11, 12, 15, 14, 17, 16, 18, 20, 19])) 
print (questao6([1, 4, 2, 3, 5, 6, 9, 7, 8, 10, 11, 14, 12, 13, 16, 15, 18, 17]))
print (questao6([1, 4, 2, 3, 5, 6, 7, 10, 8, 9, 11])) 
print (questao6([1, 3, 2, 5, 4, 7, 6, 8, 11, 9, 10, 14, 12, 13, 15, 18, 16, 17, 19, 21, 20, 22, 23, 24, 25, 26, 27, 28, 30, 29]))
print (questao6([1, 2, 5, 3, 4, 6, 10, 7, 8, 9, 11, 13, 12, 14, 16, 15, 17, 18, 19, 22, 20, 21, 23])) 
print (questao6([1, 2, 3, 4, 6, 5, 8, 7, 9, 12, 10, 11, 13, 14, 16, 15, 17, 19, 18, 20, 21, 22, 23, 26, 24, 25, 27]))



'''def questao6(q):
    subornos = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("caos")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                subornos += 1
    print(subornos)

print (questao6([1, 2, 4, 3, 6, 5, 7, 8, 12, 9, 10, 11, 14, 13, 15, 17, 16, 18, 21, 19, 20, 22, 23, 25, 24]))
print (questao6([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 19, 17, 18, 22, 20, 21, 25, 23, 24, 27, 26]))
print (questao6([1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 15, 14, 17, 16, 18, 19, 21, 20, 22, 23, 24]))
print (questao6([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 12, 11, 13, 14, 15, 16, 17, 20, 18, 19, 23, 21, 22, 24, 25]))
print (questao6([1, 2, 4, 3, 5, 6, 8, 7, 10, 9, 13, 11, 12, 15, 14, 17, 16, 18, 20, 19])) 
print (questao6([1, 4, 2, 3, 5, 6, 9, 7, 8, 10, 11, 14, 12, 13, 16, 15, 18, 17]))
print (questao6([1, 4, 2, 3, 5, 6, 7, 10, 8, 9, 11])) 
print (questao6([1, 3, 2, 5, 4, 7, 6, 8, 11, 9, 10, 14, 12, 13, 15, 18, 16, 17, 19, 21, 20, 22, 23, 24, 25, 26, 27, 28, 30, 29]))
print (questao6([1, 2, 5, 3, 4, 6, 10, 7, 8, 9, 11, 13, 12, 14, 16, 15, 17, 18, 19, 22, 20, 21, 23])) 
print (questao6([1, 2, 3, 4, 6, 5, 8, 7, 9, 12, 10, 11, 13, 14, 16, 15, 17, 19, 18, 20, 21, 22, 23, 26, 24, 25, 27]))'''

