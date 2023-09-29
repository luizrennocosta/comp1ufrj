# Ex 1
def questao1(n,ar):
    if 1<=n<=100:
        for i in range(len(ar)):
            if ar[i]>100 or ar[i]<1 or i>=n or i<0:
                return None
        ar2 = set(ar)
        parTotal = 0
        for cor in ar2:
            parTemporal = 0
            for corMeia in ar:
                if cor == corMeia:
                    parTemporal = parTemporal + 1
            parTotal = parTotal + parTemporal//2
        return parTotal

print(questao1(7,[29,29,21,37,21,5,21]))
print(questao1(10,[10,42,46,46,6,42,18,18,42,18]))
print(questao1(11,[20,35,15,15,25,40,30,20,40,45,20]))
print(questao1(7,[36,36,15,22,36,43,36]))
print(questao1(15,[28,37,28,28,37,37,37,28,19,37,37,37,37,28,28]))
print(questao1(5,[31,37,22,34,31]))
print(questao1(8,[24,14,4,24,24,14,14,24]))
print(questao1(6,[34,16,25,34,25,34]))
print(questao1(13,[20,28,20,28,44,44,44,20,20,20,20,28,36]))
print(questao1(11,[13,13,13,13,22,13,13,13,13,22,22]))
print('---------------------------------------------------')

# Ex 2
import math

def questao2(AB,BC):
    if AB<=0 or AB>1000 or BC<=0 or BC>1000:
        return None
    hip = (AB**2 + BC**2)**(1/2)
    sinAlpha = AB/hip
    AlphaPi = math.asin(sinAlpha)
    AlphaGraus = math.degrees(AlphaPi)
    NumPrimeiraCasaDecimal = (AlphaGraus*10)%10
    AlphaGrausArred = round(AlphaGraus)
    if NumPrimeiraCasaDecimal == 5:
        if AlphaGraus%2 == 0:
            AlphaGrausArred = AlphaGrausArred + 1
    return AlphaGrausArred

print(questao2(52,34))
print(questao2(91,13))
print(questao2(25,30))
print(questao2(7,50))
print(questao2(35,1))
print(questao2(35,39))
print(questao2(5,4))
print(questao2(72,38))
print(questao2(30,52))
print(questao2(2,84))
print('--------------------------------------')

# Ex 3
def questao3(stringA,stringB):
    if 1<=len(stringA)<=10000 and 1<=len(stringB)<=10000:
        vetorAlfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        vetorStringA = [0]*26
        vetorStringB = [0]*26
        vetorStringCaracNecessario = [0]*26
        stringA.lower()
        stringB.lower()
        for i in range(len(vetorAlfabeto)):
            for caractereStrA in stringA:
                if caractereStrA == vetorAlfabeto[i]:
                    vetorStringA[i] = vetorStringA[i] + 1
        for i in range(len(vetorAlfabeto)):
            for caractereStrB in stringB:
                if caractereStrB == vetorAlfabeto[i]:
                    vetorStringB[i] = vetorStringB[i] + 1 
        numeroExclusoesTotal = 0
        for i in range(len(vetorAlfabeto)):
            numeroExclusoesTemporario = 0
            if vetorStringA[i] != vetorStringB[i]:
                if vetorStringA[i] > vetorStringB[i]:
                    numeroExclusoesTemporario = vetorStringA[i] - vetorStringB[i]
                    numeroExclusoesTotal = numeroExclusoesTotal + numeroExclusoesTemporario
                    vetorStringCaracNecessario[i] = numeroExclusoesTemporario
                else:
                    numeroExclusoesTemporario = vetorStringB[i] - vetorStringA[i]
                    numeroExclusoesTotal = numeroExclusoesTotal + numeroExclusoesTemporario
                    vetorStringCaracNecessario[i] = numeroExclusoesTemporario
        return numeroExclusoesTotal

    else:
        return None

print(questao3('cgha','idge'))
print(questao3('jagii','bggad'))
print(questao3('bdecbifcg','eifgb'))
print(questao3('fcde','iaaeabba'))
print(questao3('fibj','bjhdi'))
print(questao3('gedg','jchhdaaffb'))
print(questao3('hde','ajifafjhga'))
print(questao3('egbddg','digj'))
print(questao3('dbfgbb','adccgehaj'))
print(questao3('efgie','aeedbbc'))
print('---------------------------------------------')

# Ex 4
def factorial(n):
    resultado = 1
    if n == 0 or n == 1:
        return resultado
    for i in range(n):
        resultado = resultado*(i+1)
    return resultado

def questao4(x,n):
    if type(n) != int or n < 0:
        return None
    ExpNatural = 0
    for i in range(n):
        ExpNatural = ExpNatural + (x**i)/(factorial(i))
    return ExpNatural

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
print('-----------------------------------------------')

# Ex 5
def questao5(arrayA):
    arrayB = []
    n = 0
    while n != -1:
        if n == 0:
            arrayB = arrayB + [arrayA[0]]
            if arrayA[0] == -1:
                return arrayB
            k = arrayA[0]
            n = 1
        else:
            if arrayA[k] != -1:
                arrayB = arrayB + [arrayA[k]]
                k = arrayA[k]
            else:
                arrayB = arrayB + [-1]
                n = -1
    tamanhoB = len(arrayB)
    return tamanhoB
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
print('---------------------------------------------------')

# Ex 6
def questao6(q):
    n = 0
    q1 = q[:]
    numeroSubornoTotal = 0
    filaNormal = range(1,len(q)+1)
    pos = -1
    controle = True
    while pos>=(-1*len(q)):
        if q[pos] > filaNormal[pos]:
            subornoTemporario = (pos - (-1*len(q)+q[pos]-1))*-1
            if subornoTemporario > 2:
                print('caos')
                controle = False
                break
            numeroSubornoTotal = numeroSubornoTotal + subornoTemporario
        pos = pos - 1
    if controle:
        print(numeroSubornoTotal)

questao6([1,2,4,3,6,5,7,8,12,9,10,11,14,13,15,17,16,18,21,19,20,22,23,25,24])
questao6([1,3,2,4,5,6,7,8,9,10,11,13,12,14,15,16,19,17,18,22,20,21,25,23,24,27,26])               
questao6([1,3,2,4,5,7,6,8,9,10,11,12,13,15,14,17,16,18,19,21,20,22,23,24])
questao6([1,3,2,5,4,6,7,8,9,10,12,11,13,14,15,16,17,20,18,19,23,21,22,24,25])               
questao6([1,2,4,3,5,6,8,7,10,9,13,11,12,15,14,17,16,18,20,19])
questao6([1,4,2,3,5,6,9,7,8,10,11,14,12,13,16,15,18,17])       
questao6([1,4,2,3,5,6,7,10,8,9,11])
questao6([1,3,2,5,4,7,6,8,11,9,10,14,12,13,15,18,16,17,19,21,20,22,23,24,25,26,27,28,30,29])
questao6([1,2,5,3,4,6,10,7,8,9,11,13,12,14,16,15,17,18,19,22,20,21,23])
questao6([1,2,3,4,6,5,8,7,9,12,10,11,13,14,16,15,17,19,18,20,21,22,23,26,24,25,27])

# Ex 7(bonus)
def fatorial(x):
    resultado = 1
    if x == 0 or x == 1:
        return resultado
    else:
        for i in range(1,(x+1)):
            resultado = resultado*i
        return resultado

def questao7():
    soma = 0
    for num in range(1,50001):
        somaTemporaria = 0
        num1 = str(num)
        num1 = list(num1)
        num1 = num1[::-1]
        for algarismo in num1:
            alg = int(algarismo)
            somaTemporaria = somaTemporaria + fatorial(alg)
        if somaTemporaria == num:
            soma = soma + num
    print('A soma de todos os numeros com essa propriedade é: ', soma)
    
questao7()


