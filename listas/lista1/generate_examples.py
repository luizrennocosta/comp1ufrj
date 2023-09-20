from answers import *
import random
import pickle
import string
import numpy as np

random.seed(100)


def generate_questao1_examples(n):
    exemplos = []
    for k in range(n):
        lower_bound = random.randint(1, 20)
        upper_bound = random.randint(30, 50)
        step = random.randint(1, 10)
        array_length = random.randint(5, 15)
        exemplos.append(
            random.choices(range(lower_bound, upper_bound, step), k=array_length)
        )
    return exemplos


def generate_questao2_examples(n):
    exemplos = []
    for k in range(n):
        ab = random.randint(1, 100)
        bc = random.randint(1, 100)
        exemplos.append((ab, bc))
    return exemplos


def generate_questao3_examples(n):
    exemplos = []
    for k in range(n):
        a = "".join(random.choices(string.ascii_lowercase[:10], k=random.randint(3, 10)))
        b = "".join(random.choices(string.ascii_lowercase[:10], k=random.randint(3, 10)))
        exemplos.append((a, b))
    return exemplos


def generate_questao4_examples(n):
    exemplos = []
    for k in range(n):
        x = round(random.random() * 5, 2)
        n = random.randint(1, 10)
        exemplos.append((x, n))
    return exemplos


def generate_questao5_examples(n):
    exemplos = []
    for _ in range(n):
        array_length = random.randint(5, 15)
        array = list(range(array_length))
        array[0] = -1

        perm_array = np.random.permutation(array)
        while perm_array[0] == -1:
            perm_array = np.random.permutation(array)

        exemplos.append(perm_array)
    return exemplos


def generate_questao6_examples(n):
    p_bribe = 0.4
    list_of_lines = []
    for _ in range(n):
        bribes = {}
        line_length = random.randint(5, 30)
        line = list(range(1, line_length + 1))
        for k in reversed(range(line_length)):
            if random.random() < p_bribe:
                if k > 1:
                    if line[k] not in bribes:
                        bribes[line[k]] = 1
                        line[k], line[k - 1] = line[k - 1], line[k]

                    elif bribes[line[k]] < 2:
                        bribes[line[k]] += 1
                        line[k], line[k - 1] = line[k - 1], line[k]
                    elif random.random() < 0.25:
                        bribes[line[k]] += 1
                        line[k], line[k - 1] = line[k - 1], line[k]
        list_of_lines.append(line.copy())
    return list_of_lines


def save_input_output(input, output, file):
    with open(file, "wb") as f:
        pickle.dump((input, output), f)


questoes = {}
questoes["questao1"] = []
questoes["questao2"] = []
questoes["questao3"] = []
questoes["questao4"] = []
questoes["questao5"] = []
questoes["questao6"] = []

q1_e = generate_questao1_examples(10)
q2_e = generate_questao2_examples(10)
q3_e = generate_questao3_examples(10)
q4_e = generate_questao4_examples(10)
q5_e = generate_questao5_examples(10)
q6_e = generate_questao6_examples(10)


for e in q1_e:
    questoes["questao1"].append({"input": (len(e), e), "output": questao1(len(e), e)})
for e in q2_e:
    questoes["questao2"].append({"input": e, "output": questao2(e[0], e[1])})
for e in q3_e:
    questoes["questao3"].append({"input": e, "output": questao3(e[0], e[1])})
for e in q4_e:
    questoes["questao4"].append({"input": e, "output": questao4(e[0], e[1])})
for e in q5_e:
    questoes["questao5"].append({"input": e, "output": questao5(e)})
for e in q6_e:
    questoes["questao6"].append({"input": e, "output": questao6(e)})


with open("examples.txt", "w") as f:
    f.write("\n ****** Questão 1 ******\n")
    for ex in q1_e:
        f.write(f"Entrada: ({len(ex)}, {ex}) \t Saída: {questao1(len(ex), ex)}\n")

    f.write("\n ****** Questão 2 ******\n")
    for ex in q2_e:
        f.write(f"Entrada: ({ex[0]}, {ex[1]}) \t Saída: {questao2(ex[0], ex[1])}\n")

    f.write("\n ****** Questão 3 ******\n")
    for ex in q3_e:
        f.write(f"Entrada: ({ex[0]}, {ex[1]}) \t Saída: {questao3(ex[0], ex[1])}\n")

    f.write("\n ****** Questão 4 ******\n")
    for ex in q4_e:
        f.write(f"Entrada: ({ex[0]}, {ex[1]}) \t Saída: {questao4(ex[0], ex[1])}\n")

    f.write("\n ****** Questão 5 ******\n")
    for ex in q5_e:
        f.write(f"Entrada: ({ex}) \t Saída: {questao5(ex)}\n")

    f.write("\n ****** Questão 6 ******\n")
    for ex in q6_e:
        f.write(f"Entrada: ({ex}) \t Saída: {questao6(ex)}\n")


with open("questoes_pickle", "wb") as f:
    pickle.dump(questoes, f)
