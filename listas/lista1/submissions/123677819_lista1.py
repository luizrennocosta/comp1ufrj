def questao1(N,ar):
    #estabelecendo uma variável para a contagem de pares
    pares = 0
    #a função irá analisar cor por cor, e para manter o registro das já analisadas, estabeleceremos uma lista
    cor_analisada=[]
    for cor in ar:
        if cor in cor_analisada:
            #se estiver na lista de cores analisdas, é retirada e um par é contado
            pares += 1
            cor_analisada.remove(cor)
        else:
            cor_analisada.append(cor)
    return pares

import math
def questao2(AB,BC):
    #note que em um triangulo retangulo, a mediana sempre tem medida igual a metade da hipotenusa, gerando dois triangulos isosceles BMC e BMA.
    #Portanto, o angulo BCM é igual a theta, e sua tangente é BA/BC
    return round(math.degrees(math.atan(AB/BC)))

def questao3(string_a,string_b):
    exclusivos = []
    for n in string_a:
            if n not in string_b:
                exclusivos.append(n)
    for n in string_b:
            if n not in string_a:
                exclusivos.append(n)
    
    return len(exclusivos)

def factorial(p):
    #funcao auxiliar factorial
    if p==0:
        return 1
    else:
        return p*factorial(p-1)

def fator(x,k):
    #funcao auxiliar para montar os termos
    return (x**k)/factorial(k)

def questao4(x,n):
    resultado = 0
    for i in range(n):
        resultado += fator(x,i)
    return resultado

def questao5(A):
    B = []
    for K in A:
        if A[K]!=-1:
            B.append(K)
        else:
            break
    return len(B)
    



def questao6(q):
    subornos=0
    for i in range(len(q)):
        if q[i]>i+3:
            print("caos")
            return
        else:
            for k in range(max(0,q[i]-2),i):
                if q[k]>q[i]:
                    subornos+=1
    print (subornos)  
    


def questao7():
    lista = []
    limite = 50000
    for n in range(1, limite):
        b = str(n)  # converte o numero em uma string
        c = 0
        for i in range(len(b)):
            c += factorial(int(b[i]))
        if c == n:
            lista.append(n)
    return sum(lista)
    
        
        
    
    
    

            
    
    
    
