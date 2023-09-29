'''QUESTAO 1'''
def questao1(n,ar): 
    impares = []
    '''lista mutavel para ver quantos ficam de sobra dos pares de meia'''
    for i in range (n):
        if ar.count(ar[i])%2 == 1 and ar[i] not in impares:
            '''se o resto for 1 e se já não ter contado o número antes, então:'''
            impares.append(ar[i])
    pares = (n - len(impares))//2 
    return pares

print ('QUESTAO1')
resultado = questao1(7,[29,29,21,37,21,5,21])
print (f'O(s) número(s) de pare(s) de meia(s) é: {resultado}')

'''QUESTAO2'''
def questao2(AB,BC):
    import math
    AC = (AB**2+BC**2)**0.5 #1-Achar a hipotenusa
    x = ((BC/AC)) #2-Achar cosseno do angulo
    arcosseno = math.acos(x) 
    graus = math.degrees(arcosseno)
    angulo = round(graus) #Arredondando para inteiro
    

    return angulo
print('QUESTAO2')
result = questao2(52,34)
print (f'O angulo é:{result}')

'''QUESTAO 3'''
def questao3(string_a,string_b):
    ps = 0
    elementos_iguais = []
    iguais = [elemento for elemento in string_a if elemento in string_b]

    if len(iguais) == 0:
        alteracoes =  len(string_a) + len(string_b)
    else:
        for elemento in iguais:
            if iguais.count(elemento) > 1 and elemento not in elementos_iguais:
                elementos_iguais.append(elemento)
        alteracoes = len(string_a) + len(string_b) - 2*((len(iguais) - len(elementos_iguais)))
    

    return alteracoes
    
print ('QUESTAO 3')
print (questao3("efgie", "aeedbbcc"))


'''QUESTAO 4'''
def factorial (n):
    m=1
    ft=1
    while m<=n:
        ft = ft*(m)
        m = m+1
    return ft

def questao4(x,n):
    pos = 0
    exponencial = 0
    while pos<n:
        exponencial = exponencial + ((x**pos)/(factorial(pos)))
        pos = pos+1
    
    return exponencial

print('QUESTAO4')
valor = questao4(1.47,7)
print(f'O e^x é {valor}')

'''QUESTAO 5'''
def questao5(arrayA):
    comprimento = 0
    ps = 0
    while ps != -1: #enquanto ps nao chega no ultimo termo da lista
        comprimento += 1 #add mais um no compri
        ps = arrayA[ps] #analisa agora qual e o termo relativo a ps inicial e vai/
                        #até a posicao do termo
    return comprimento

print ('QUESTAO 5')
comprimento = questao5([4 ,2, 9, 5, 11, 7, 8, 10, 3, 6, 1, -1])
print (f'O comprimento do array é {comprimento}')


'''QUESTAO 6'''

def questao6(fila_mod):
    subornos = 0
    
    for i in range(len(fila_mod)-1, -1, -1):
        if fila_mod[i] - (i+1) > 2:
            print("caos")
            return
        
        for j in range(max(0, fila_mod[i]-2), i):
            if fila_mod[j] > fila_mod[i]:
                subornos += 1
    print(subornos)

print (questao6([1, 2, 4, 3, 6, 5, 7, 8, 12, 9, 10, 11, 14, 13, 15, 17, 16, 18, 21, 19, 20, 22, 23, 25, 24]))
print (questao6(([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 19, 17, 18, 22, 20, 21, 25, 23, 24, 27, 26])))
print (questao6([1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 15, 14, 17, 16, 18, 19, 21, 20, 22, 23, 24]))
print (questao6(([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 12, 11, 13, 14, 15, 16, 17, 20, 18, 19, 23, 21, 22, 24, 25]) ))
