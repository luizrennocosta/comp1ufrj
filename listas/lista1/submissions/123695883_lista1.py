import math

#Questão 1
def questao1(qnt_meias, meias):
    if len(meias) == qnt_meias:    
        meias_iguais = 0
        contador = 0
        lista_numeros_ja_usados = []
        numero_ja_usado = False
        pares = 0
        for meia in meias:
            for numero in lista_numeros_ja_usados:
                if numero == meia:
                    numero_ja_usado = True
            if numero_ja_usado == False:
                while contador < len(meias):
                    if meia == meias[contador]:
                        meias_iguais += 1
                    contador += 1
                pares = pares + meias_iguais // 2
                lista_numeros_ja_usados.append(meia)
                meias_iguais = 0
                contador = 0
                print(lista_numeros_ja_usados)
            else: numero_ja_usado = False             
        return pares
    else:
        return print("Quantidade de meias não bate com a quantidade de meias informadas.")

#Questão 2
def questao2(AB,BC):
    AC = math.sqrt(AB**2 +BC**2)
    MC = AC/2
    angBCM = math.atan(AB/BC)
    BM = math.sqrt(BC**2 + MC**2 - 2*(BC*MC*(math.cos(angBCM))))
    angulo = math.degrees(math.asin((math.sin(angBCM)*MC)/BM))
    if (angulo - int(angulo)) < 0.5:
        angulo = int(angulo)
    else:
        angulo = math.ceil(angulo)
    return angulo

#Questão 3
def questao3(string_a,string_b):
    qnt_letras_comuns = 0
    for letra_string_a in string_a:
        for letra_string_b in string_b:
            if letra_string_a == letra_string_b:
                qnt_letras_comuns += 1
                break
    retirar_a = len(string_a)-qnt_letras_comuns
    retirar_b = len(string_b)-qnt_letras_comuns
    retirar_total = retirar_a + retirar_b
    return retirar_total

#Questão 4
def questao4(x_expoente,quantidade_n_elem):

    def factorial(n):
        fatorial = 1
        if n > 0:
            while n > 1:
                fatorial = fatorial*(n)*(n-1)
                n -= 2
        elif n == 0: fatorial = 1
        else: None
        return fatorial
    
    funcao_expon = 0    
    if quantidade_n_elem >= 0:
        while quantidade_n_elem >= 1:
            funcao_expon = (x_expoente**(quantidade_n_elem-1)/(factorial(quantidade_n_elem-1))) + funcao_expon
            quantidade_n_elem -= 1
        return funcao_expon
    else:
        return print('Valor informado inválido.')

#Questão 5
def questao5(array_A):
    lista_final = []
    membro_lista = 0
    for c in array_A:
        lista_final.append(array_A[membro_lista])
        membro_lista = array_A[membro_lista]
        if membro_lista == -1:
            break
    comprimento_lista_final = len(lista_final)
    return comprimento_lista_final

#Questão 6 Não consegui fazer esse código rodar perfeitamente, procurei bastante o erro e não achei :(
def questao6(fila):
    contador = len(fila)
    subornos = 0
    fila_em_ordem = [None]*len(fila)
    for pessoa in reversed(fila):
        if pessoa == contador:
            contador -= 1
        elif pessoa < contador:
            if pessoa == (contador-1):
                print(pessoa)
                subornos +=1
                fila_em_ordem[pessoa-1] = pessoa
                contador -= 1
            else:
                if pessoa == (contador-2):
                    subornos +=2
                    fila_em_ordem[pessoa-1] = pessoa
                    contador -= 1
                else:
                    subornos = 'caos'
                    break
        else:
            quanto_andou_esquerda = pessoa - contador
            if quanto_andou_esquerda <= 2:
                subornos += quanto_andou_esquerda
                contador -= 1
            else:
                subornos = 'caos'
                break
    return subornos






