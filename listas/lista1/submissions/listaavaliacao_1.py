#lista de exercícios 1 : Rodrigo Oliveira do Nascimento, DRE - 123672615

#questao 1

def questao1 (qtd, lista):
    pares = [] #lista que vai ter as posições de todos os pares de meias possíveis
    contagem1=0
    contagem2=1
    if 1<=qtd<=100:
        while contagem1<qtd:
            contagem2=1
            while contagem2<qtd:
                if lista[contagem1]==lista[contagem2] and (contagem1!=contagem2):
                    pares+=[(contagem1,contagem2)]
                contagem2+=1
            contagem1+=1
        lista = [] #lista que tem os pares de meia sem repetir 
        contagem1=0
        contagem2=0
        while contagem1<len(pares):
            if pares[contagem1][0] not in lista and  pares[contagem1][1] not in lista:
                lista+=pares[contagem1]
            contagem1+=1
        qtdpares = len(lista)/2
        return (qtdpares)
    else:
        print ('parâmetro inválido')

#print (questao1(7,[1, 2, 1, 2, 1, 3, 2]))
#print (questao1(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

#questao 2
     
def questao2 (ladoab, ladobc):
    import math
    if 0<ladoab<=1000 and 0<ladobc<=1000:
        angrad = math.atan2(ladoab, ladobc) #em radianos
        anggraus= math.degrees(angrad) #em graus
        res = round(anggraus)
        return (res)
    
#print (questao2(10,10))
#print (questao2(1,100))

#questao 3

def questao3 (string1, string2):
    if 1<=len(string1)<=10000 and 1<=len(string2)<=10000:
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        qtdletrasa = [0]*len(alfabeto)
        qtdletrasb = [0]*len(alfabeto)
        #a ideia é checar quantidade de cada letra por string e ver quais as diferenças.
        str1 =[]
        str2 = []
        for letra in string1:
            str1 += [letra]
        for letra in string2:
            str2+= [letra]
        contagem1 = 0
        contagem2 = 0
        while contagem1<len(str1):
            while contagem2<len(alfabeto):
                if str1[contagem1]==alfabeto[contagem2]:
                    qtdletrasa[contagem2]+=1
                contagem2+=1
            contagem2=0
            contagem1+=1
        contagem1 = 0
        contagem2 = 0
        while contagem1<len(str2):
            while contagem2<len(alfabeto):
                if str2[contagem1]==alfabeto[contagem2]:
                    qtdletrasb[contagem2]+=1
                contagem2+=1
            contagem2=0
            contagem1+=1
        contagem=0
        qtdletrasdif = 0 #quantidade de letras diferentes entre cada string, letras para serem retiradas
        for quantidade in qtdletrasa:
            if quantidade!= qtdletrasb[contagem]:
                if quantidade>qtdletrasb[contagem]:
                    qtdletrasdif+= (quantidade) - (qtdletrasb[contagem])
                elif quantidade<qtdletrasb[contagem]:
                    qtdletrasdif+= (qtdletrasb[contagem]) - (quantidade)
            contagem+=1       
        return (qtdletrasdif)

#print (questao3('abacaxi', 'abobora'))
#print (questao3('cde', 'abc'))

#questão 4
    
def fatorial (num):
    if num==0:
        return (1)
    if type(num)==int:
        result=1
        n=num
        while n>=1:
            result = result * n
            n=n-1
    return (result)

def questao4 (num, qtd):
    n=0
    soma=0
    while n<qtd:
        soma+= (num**n)/fatorial(n)
        n+=1
    return (soma)

#print (questao4(2,10))
#print (questao4(5,100))
#print (questao4(10,100))

#questão5

def questao5(array):
    posicao = 0
    qtdno=1
    listaposicoes = []
    listajatem = []
    while posicao<len(array):
        listaposicoes+=[posicao]
        posicao+=1
    posicao=0
    while qtdno<len(array):
        if array[posicao]==-1:
            break
        if (array[posicao] in listaposicoes) and (array[posicao] not in listajatem):
            qtdno+=1
            posicao=array[posicao]
            listajatem+=[posicao]
        else:
                posicao+=1
    return (qtdno)

#print (questao5([1,4,-1,3,2]))

#questao6

def questao6(fila):
    filacerta = [] #comparar com a fila pra saber quantos subornos ocorreram
    contagem=0
    valor=1
    while contagem<len(fila):
        filacerta+=[valor]
        contagem+=1
        valor+=1
    contagem=0
    subornos=[]
    while contagem<len(fila):
        pulo = fila[contagem]- filacerta[contagem]
        subornos+=[pulo]
        contagem+=1
    soma=0
    contagem=0
    while contagem<len(subornos):
        if subornos[contagem]>2:
            print ('caos')
            return None
            break
        elif subornos[contagem]>=0 and subornos[contagem]<=2:
            soma+=subornos[contagem]
        elif subornos[contagem]<0:
            soma+=(subornos[contagem]*-1)
        contagem+=1
        res = soma/2
    print (int(res))
    
#print (questao6([2, 1, 5, 3, 4]))
#print (questao6([2, 5, 1, 3, 4]))
#print (questao6([5, 1, 2, 3, 7, 8, 6, 4]))
#print (questao6([1, 2, 5, 3, 7, 8, 6, 4]))

#questao7
    
def fatorial (num):
    if num==0:
        return (1)
    if type(num)==int:
        result=1
        n=num
        while n>=1:
            result = result * n
            n=n-1
    return (result)

def curioso(num):
    digitos= str(num)
    soma=0
    for dig in digitos:
        soma+=fatorial(int(dig))
    if soma==num:
        return True
    
def questao7(n):
    if n < 10000000:
        contagem=0
        soma=0
        while contagem<n:
            if curioso(contagem) == True:
                soma+=contagem
            contagem+=1
        return (soma)

#com n<=1000 dá sempre 148 pq os únicos numeros são 1,2 e 145
#com n indo até 10 milhões da 40733
#para n maiores meu pc não ta conseguindo calcular mas acho que deve se manter constante 
#print (questao7(10000000))



    

