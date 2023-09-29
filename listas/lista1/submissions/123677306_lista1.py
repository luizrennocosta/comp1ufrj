import math

def questao1(n,ar):
    pares = 0
    cores=[]
    for i in range(n):
        novo = True
        for j in range (i):
            if ar[i]==ar[j]:
                novo = False
        if novo==True:
            cores+=[ar[i]]
    for k in cores:
        quant_elementos_por_cor = 0
        for l in ar:
            if k == l:
                quant_elementos_por_cor +=1
        pares += quant_elementos_por_cor //2 
    return pares

def questao2(ab,bc):
    ac=(((ab)**2 + (bc)**2)**(1/2))
    mc=ac/2
    am=ac/2
    bm=((mc)*(am))**(1/2)
    cosMBC=((bm)**2 + (bc)**2 - (mc)**2)/(2*bm*bc)
    angulo_radiano=math.acos(cosMBC)
    angulo_grau=math.degrees(angulo_radiano)
    if (angulo_grau - math.trunc(angulo_grau))>=(0.5):
        return (math.trunc(angulo_grau) + 1)
    else:
        return math.trunc(angulo_grau)

def questao3(a,b): 
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    vetor_a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    vetor_b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for elementoA in a:
        vetor_a[alfabeto.index(elementoA)]+=1
    for elementoB in b:
        vetor_b[alfabeto.index(elementoB)]+=1   
    letras_diferentes=0
    for j in range(len(vetor_a)):
        if (vetor_a[j]>=vetor_b[j]):
            letras_diferentes+=(vetor_a[j]-vetor_b[j])
        else:
            letras_diferentes+=(vetor_b[j]-vetor_a[j])
    return letras_diferentes

def factorial(n): 
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    return fact
def questao4(x,n):
    soma=0
    i=0
    while i<(n):
        soma+=(x**i)/(factorial(i))
        i+=1
    return soma

def questao5(ar):
    comprimento=1 
    i=0
    while ar[i]!=-1:
        comprimento+=1
        i=ar[i]
    return comprimento

def questao6(q):
    fila_original=[]
    for i in range (1,len(q)+1,1):
        fila_original+=[i]
    subtracao_listas=[]
    for j in range (len(q)):
        subtracao_listas+=([q[j]-fila_original[j]])
    subornos=0
    ehmaiorq2=False
    for k in range (len(q)):
        if subtracao_listas[k]>0:
            subornos+=subtracao_listas[k]
            if subtracao_listas[k]>2:
               ehmaiorq2=True
    if ehmaiorq2==True:
        print("caos")
    else:
        print(subornos)    
    
def questao7():
    eh_curioso=0
    for num in range(0,50001,1):
        num_string=str(num)
        num_lista=[]
        for i in range(len(num_string)):
            num_lista+=[int(num_string[i])]
        soma_fact_dig=0
        for elemento in num_lista:
            soma_fact_dig+=factorial(elemento)
        if soma_fact_dig == num:
            eh_curioso+=num
    return eh_curioso