import random
from answers import *
import pickle


def gerar_exemplos():
    exemplos = {f"questao{i}": [] for i in range(1, 6)}

    # Exemplos para questao1
    times = ['Knicks', 'Raptors', 'Heat', 'Bulls', 'Hawks', 'Celtics']
    for _ in range(10):
        jogos = random.sample([f'{t1} X {t2}' for t1 in times for t2 in times if t1 != t2], 5)
        resultados = {jogo: random.choice([jogo.split(' X ')[0], jogo.split(' X ')[1]]) for jogo in jogos}
        time_escolhido = random.choice(times)
        entrada_q1 = (resultados, time_escolhido)
        saida_q1 = questao1(*entrada_q1)
        exemplos['questao1'].append({'input': entrada_q1, 'output': saida_q1})

    # Exemplos para questao2
    alunos = ['Geto', 'Gojo', 'Yuji', 'Kashimo', 'Yuta', 'Maki', 'Megumi', 'Nobara']
    for _ in range(10):
        notas_alunos = {nome: [round(random.uniform(0, 10),2) for _ in range(2)] for nome in [random.choice(alunos) for _ in alunos]}
        entrada_q2 = notas_alunos
        saida_q2 = questao2(entrada_q2)
        exemplos['questao2'].append({'input': entrada_q2, 'output': saida_q2})

    # Exemplos para questao3
    palavras_base = ['aka', 'shiro', 'murasaki', 'ao', 'midori', 'kuro']
    for _ in range(10):
        palavras = palavras_base + [random.choice(palavras_base) for _ in range(len(palavras_base))]
        random.shuffle(palavras)
        entrada_q3 = palavras
        saida_q3 = questao3(entrada_q3)
        exemplos['questao3'].append({'input': entrada_q3, 'output': saida_q3})

    # Exemplos para questao4
    for _ in range(10):
        numeros = [round(random.uniform(-10, 10), 2) for _ in range(5)]
        entrada_q4 = numeros
        saida_q4 = questao4(entrada_q4)
        exemplos['questao4'].append({'input': entrada_q4, 'output': saida_q4})

    # Exemplos para questao5
    # Como a questão 5 trabalha com arquivos, vou apenas fornecer um exemplo estático 10 vezes.
    for f_num in range(10):
        nome_arquivo = f"notas_exemplo{f_num}.txt"
        with open(nome_arquivo, 'w') as f:
            f.write("DRE,notas\n")
            for _ in range(10):  # 4 alunos por arquivo
                dre = str(_)*7
                notas = ",".join([str(random.randint(0, 10)) if random.random() > 0.2 else 'F' for _ in range(6)])
                f.write(f"{dre},{notas}\n")
        entrada_q5 = nome_arquivo
        saida_q5 = questao5(entrada_q5)
        exemplos['questao5'].append({'input': entrada_q5, 'output': saida_q5})

    return exemplos

exemplos_gerados = gerar_exemplos()

with open("questoes_pickle", "wb") as f:
    pickle.dump(exemplos_gerados, f)

with open('examples.txt', 'w') as ex_f:
    for questao, lista_dados in exemplos_gerados.items():
        ex_f.write(f"\n********* Questão {questao[-1]} *********\n")
        for i, dados in enumerate(lista_dados, 1):
            ex_f.write(f"Entrada: {dados['input']}\n")
            ex_f.write(f"Saída: {dados['output']}\n\n")