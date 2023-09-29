def questao1 (n,list):
    if n<=0 or n>=101:
        print('erro, insira um valor maior que zero e menor que 101')
        return questao1
    if isinstance(n,int):
        list.sort()
        pares = 0
        i = 0
        while i < n-1:
            if list[i] == list[i+1]:
                pares = pares+1
                i = i+2
            else:
                i = i+1
        return pares
    else:
       print('n precisa ser inteiro')
       return questao1
def questao2(AB,BC):
    import math
    if 0 < AB < 10**3 and 0 < BC < 10**3:
        ARCTAN = math.atan2(AB,BC)
        ANGULOMBC = round(math.degrees(ARCTAN))
        return ANGULOMBC
print (questao2(52,34))
print (questao2(92,13))
def questao3 (a,b):   
    lista1 = list(a)
    lista2 = list(b)
    quantidadedletrasemcomum = 0
    i = 0
    daybreak = len(lista2)
    nightfall = len(lista1)
    while(i < daybreak):
        if (lista2[i] in lista1):
            quantidadedletrasemcomum +=1
        i+=1
    removiveist = nightfall + daybreak - 2* quantidadedletrasemcomum
    return removiveist
def factorial (n):
    result = 1
    while n >= 1:
        result = result*n
        n = n - 1
    return result
def questao4 (x,n):
    result = 0
    i = 0
    while i < n:
        result += x**i/factorial(i)
        i += 1
    return result
def questao5 (a):
    comprimento = 0
    i = 0
    while i < len(a):
        if a[i] == -1:
            comprimento += 1
            break
        else:
            comprimento += 1
            i = a[i]
    return comprimento
def questao6(q):
    caos = False
    subornos = 0
    i = 0
    while i < len(q):
        if q[i] - (i + 1) > 2:
            caos = True
            break
        j = max(0, q[i] - 2)
        while j < i:
            if q[j] > q[i]:
                subornos += 1
            j += 1
        i += 1
    if caos:
        print ('caos')
    else:
        print(subornos)
def questao7(n):
    total = 0

