#Questao 1

def questao1(n, ar):

    if 1<=n<=100:
        contagem = 0
        maior_numero = 0
        while contagem<n:
            if ar[contagem]>maior_numero:
                maior_numero = ar[contagem]
            contagem +=1

        contagem = 0    
        select_meia= [0] * (maior_numero +1) 
        while contagem<n:
            select_meia[ar[contagem]] +=1
            contagem+=1

        contagem = 0
        pares = 0
        while contagem < len(select_meia):
            pares += select_meia[contagem]//2
            contagem += 1
        return pares

#Questao2
def questao2(ab,bc):
    import math
    if 0<ab<=10**3 and 0<bc<=10**3:
        angulo_bm = math.degrees(math.atan2(ab,bc))
        return round(angulo_bm)
        
#Questao3

def questao3(string_a,string_b):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pos = 0
    lista_letras_a = [0] * len(alfabeto)
    lista_letras_b = [0] * len(alfabeto)
    for caractere in string_a:
        for letra in alfabeto:
             if caractere == letra:
                 lista_letras_a[pos]+=1

             pos+=1
        pos = 0
    pos = 0        
    for caractere in string_b:
        for letra in alfabeto:
            if caractere == letra:
                 lista_letras_b[pos]+=1

    
            pos +=1
        pos = 0


    contagem = 0
    diferenca = 0
    while contagem<len(lista_letras_a):
        if lista_letras_a[contagem]!=lista_letras_b[contagem]:
            if lista_letras_a[contagem]>lista_letras_b[contagem]:
                diferenca += lista_letras_a[contagem] - lista_letras_b[contagem]
            elif lista_letras_b[contagem] > lista_letras_a[contagem]:
                diferenca += lista_letras_b[contagem] - lista_letras_a[contagem]

        contagem +=1
    return diferenca
   
#Questão 4

def factorial(n):
    produto = 1
    if n == 0:
        return 1
    else:
        while n>1:
            produto*=n
            n-=1
    return produto

def questao4(x,n):
    exponencial = 0
    contagem = 0
    while contagem<n:
        resultado = (x**(contagem))/factorial(contagem)
        exponencial += resultado
        contagem+=1
    return exponencial

#Questão 5

def questao5(array):
    contagem = 0
    lista_pos = []
    quantidade_nos = 1
    while contagem < len(array):
        lista_pos += [contagem]
        contagem+=1
    
    contagem=0
    while quantidade_nos<len(array):
        if array[contagem] == -1:
            break
        else:
            if(array[contagem] in lista_pos):
                quantidade_nos+=1
                contagem=array[contagem]
    return quantidade_nos

#Questão 6
def questao6(lista_pessoas):
    contagem = 1
    lista_organizada = []
    while contagem <= len(lista_pessoas):
        lista_organizada += [contagem]
        contagem +=1

    contagem = 0
    quantidade_subornos = 0
    while contagem < len(lista_organizada):
        suborno = lista_pessoas[contagem] - lista_organizada[contagem]
        if suborno > 2:
            return print("caos")
        elif 0< suborno <= 2:
            quantidade_subornos += suborno
        else:
            contagem += 1
            continue
        contagem+=1
    return print(quantidade_subornos)

#print(questao6([1, 2, 4, 3, 6, 5, 7, 8, 12, 9, 10, 11, 14, 13, 15, 17, 16, 18, 21, 19, 20, 22, 23, 25, 24]))
#Questao7

def curioso(num):
    num_string = str(num)
    numero_curioso = 0
    for algarismo in num_string:
        factorial_algarismo = factorial(int(algarismo))
        numero_curioso += factorial_algarismo
    return numero_curioso
    
def questao7():
        contagem = 0
        soma = 0
        numero = 50000
        while contagem < numero:
            n_curioso = curioso(contagem)
            if n_curioso == contagem:
                soma+=contagem
            contagem +=1
        return soma

#print(questao7(150))
    












    

