# questao1.py
def questao1(dic, time):
    vitorias = []
    for jogo, vencedor in dic.items():
        if vencedor == time:
            vitorias.append(jogo)
    return vitorias

# questao2.py
def questao2(dic_notas):
    dic_medias = {}
    for aluno, notas in dic_notas.items():
        media = sum(notas) / len(notas)
        dic_medias[aluno] = media
    return dic_medias

# questao3.py
def questao3(lista_palavras):
    contagem = {}
    resultado = []
    for palavra in lista_palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
            resultado.append(1)
        else:
            indice = list(contagem.keys()).index(palavra)
            resultado[indice] += 1
    return resultado

# questao4.py
def questao4(lista_numeros):
    resultado = []
    for num in lista_numeros:
        try:
            valor = float(num)
            inverso = 1/valor
            resultado.append(inverso)
        except ValueError:
            return -1
        except ZeroDivisionError:
            resultado.append('inf')
    return resultado

# questao5.py
def questao5(arquivo):
    medias = {}
    with open(arquivo, 'r') as f:
        next(f)  # Ignora o cabeçalho
        for linha in f:
            partes = linha.strip().split(',')
            dre = int(partes[0])
            notas = partes[1:]
            notas = [0 if n == 'F' else float(n) for n in notas]
            media = sum(notas) / len(notas)
            medias[dre] = round(media, 2)
    return medias
