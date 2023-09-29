# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:28:42 2023

@author: young joojo
"""
def questao1(n,ar):
    n=len(ar)
    comparacao=100*[0]
    if 1<=n<=100:
        for i in range(n):
            if 1<=ar[i]<=100:
                comparacao[ar[i]]+=1
            else:
                print("ERROR")
        iguais=0
        for i in range(len(comparacao)):
            iguais+=comparacao[i]//2
    else:
        print("ERROR")
    return iguais
def questao2(AB,BC):
    import math
    if 0<AB<=10**3 and 0<BC<=10**3:
        arcotangente=math.atan2(AB,BC)
        MBC=math.degrees(arcotangente)
        MBCarredondado=round(MBC,0)
    return MBCarredondado
def questao3(stra,strb):
    alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    tamanho=len(alf)
    i = 0
    vazio_a = [0] * tamanho
    vazio_b = [0] * tamanho
    for crc in stra:
        for a in alf:
             if crc == a:
                 vazio_a[i]+=1
             i+=1
        i = 0
    i = 0        
    for crc in strb:
        for a in alf:
            if crc == a:
                 vazio_b[i]+=1
            i +=1
        i = 0
    result= 0
    i=0
    for i in range(tamanho):
        if vazio_a[i]!=vazio_b[i]:
            if vazio_a[i]>vazio_b[i]:
                result += vazio_a[i] - vazio_b[i]
            elif vazio_b[i] > vazio_a[i]:
                result += vazio_b[i] - vazio_a[i]
        i+=1
    return result
def factorial(n):
    fatorial=0
    i=1
    fatorial=1
    if n==0:
        fatorial=1
        return fatorial
    while i <= n:
        fatorial *= i
        i += 1
    return fatorial
def questao4(x,n):
    exponencial=0
    for i in range(n):
        exponencial+=(x**i)/factorial(i)
    return exponencial
def questao5(lista):
    tamanho=len(lista)
    index=0
    contador=0
    while index<(tamanho):
        if lista[index]==-1:
            contador+=1
            break
        else:
            contador+=1 
            index=lista[index]
    return contador           
def questao6(q):
    tamanho= len(q)
    ordenada=tamanho*[0]
    comparacao=tamanho*[0]
    contagem=0
    verdadeiro=0
    for i in range(tamanho):
        ordenada[i]=i+1
    for i in range(tamanho):
        comparacao[i]=q[i]-ordenada[i]
    for i in range(tamanho):
        if comparacao[i]>2:
            print("caos")
            verdadeiro=1
            break
        elif 0<comparacao[i]<=2:
            contagem+=comparacao[i]
    if verdadeiro!=1:
        print(contagem)
