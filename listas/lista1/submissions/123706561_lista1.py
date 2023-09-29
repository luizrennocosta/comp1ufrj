 
def questao1(n, ar):
    cores = [0] * 101
    for cor in ar:
        cores[cor] += 1
    pares = 0
    for cont in cores:
        pares += cont // 2

    print(pares)
    return pares

def qustao2(AB,BC):
    AB = float(input("Digite o comprimento AB: "))
    BC = float(input("Digite o comprimento BC: "))
    while (AB < 0 or AB > 1000):
        AB = float(input("Digite o comprimento AB novamente (não pode ser menor que 0 ou maior que 1000): "))
    while (BC < 0 or BC > 1000):
        BC = float(input("Digite o comprimento BC (não pode ser menor que 0 ou maior que 1000): ")) 
    angle_MBC_rad = math.atan(AB / BC)
    angle_MBC_deg = math.degrees(angle_MBC_rad)
    return angle_MBC_deg

def questao3(a, b):
    lista_a = [0] * 26
    lista_b = [0] * 26
    vetor = ord('a')
    for letra in a:
        lista_a[ord(letra) - vetor] += 1 
    for letra in b:
        lista_b[ord(letra) - vetor] += 1
    deletions = 0
    for i in range(26):
        deletions += abs(lista_a[i] - lista_b[i])
    
    print(deletions)
    return deletions

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
    return fatorial

def questão4(x, n):
    soma = 0
    for valor in range(n):
        calculo = (x**i)/fatorial(i)
        resultado += calculo
    return resultado 

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
    fila_atual=[]
    for x in range (len(q)):
        fila_atual+=([q[x]-fila_original[x]])
    subornos=0
    resultado=False
    for y in range (len(q)):
        if fila_atual[y]>0:
            subornos+=fila_atual[y]
            if fila_atual[y]>2:
               resultado=True
    if resultado==True:
        print("caos")
    else:
        print(subornos)    
   
def quetao7():
    limite = 50000
    soma_total = 0
    for numero in range(0, limite):
        digitos = [int(digito) for digito in str(numero)]
        soma_fatoriais = sum([math.factorial(d) for d in digitos])
        if soma_fatoriais == num:
            soma_total += 1
    return soma_total
