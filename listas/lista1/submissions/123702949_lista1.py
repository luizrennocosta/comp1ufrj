#1-------------------------------------------

num=15
meias=[1,2,4,7,3,4,7,3,6,5,5,5,6,8,2]

def questao1(n,ar):
    num_pares=0
    for i in range(1,n+1):
    #vai verificar quantas meias tem atraves do numero da cor, a divisao eh pra separar em pares
        x=ar.count(i)
        if x >= 2:
            qtdx=int(x/2)
            num_pares+=qtdx
    return num_pares

print(questao1(num,meias))


#2-------------------------------------------

x=5
y=5
print('questao 2')
import math
def questao2(AB,BC):
    #definindo q os pontos ab e bc estao nos eixos x e y, as coordenadas ficariam (0,AB) (BC,0) entao nao criei variaveis separadas para eles ja que nao interferem nas operaçoes
    M=(BC/2,AB/2)
    tan_mbc=math.atan2(M[0],M[1])
    tan_mbc=round(math.degrees(tan_mbc))
    return tan_mbc

print(questao2(y,x))


#3-------------------------------------------


A='abcde'
B='bcedj'
def questao3(a,b):
    list_a=list(a)
    list_b=list(b)
    contador=0
    for letra in list_a:
        if (letra in list_b)==False:
            list_a.remove(letra)
            contador+=1
    for letra in list_b:
        if(letra in list_a)==False:
            list_b.remove(letra)
            contador+=1
    list_a=" ".join(list_a)
    list_b=" ".join(list_b)
    return (contador)

print(questao3(A,B))


#4-------------------------------------------

arg=5
qtd=8
#calcula o fatorial de um numero
def factorial(n):
    if n==0:
        return 1
    n_fact=1
    for i in range(1,n+1):
        n_fact *= i
    return n_fact

def questao4(x,n):
    exp_x=1
    for i in range(n):
        exp_x+=x**i/factorial(i)
    return exp_x

print(questao4(arg,qtd))


#5-------------------------------------------

A=[1,4,-1,3,2]
def questao5(A):
    n = len(A)  
    contador = 0  
    indice = 0  

    while indice != -1:
        contador += 1  
        indice = A[indice]  
    return contador

print(questao5(A))


#6-------------------------------------------


listx=[2, 1, 3, 4, 5, 6, 7, 8]
def questao6(lista):
    lista_base=[]
    suborno=0
    posiçao=0
    pos=0
    for i in range(1,(len(lista))+1):
        lista_base.append(i)
    
    for j in lista:
        posiçao=lista.index(j)
        if j!=lista_base[posiçao]:
            pos=lista_base.index(j)
            suborno=abs(posiçao-pos)
            if suborno>2:
                return 'caos'
            
    return suborno
       
print(questao6(listx))


#7 BONUS-------------------------------------




    