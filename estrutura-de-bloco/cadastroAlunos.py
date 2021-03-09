exit = "N"
alunos = []


while exit == "N" or exit == "n":
    somaNota = 0
    nome = str(input("Digite um nome: "))

    for x in range(4):
        somaNota += float(input("Digite uma nota: "))

    media = somaNota//4
    alunos.append({"nome": nome, "media": media})
    exit = str(
        input("Deseja encerrar? S (sim) ou N (não)"))

for x in alunos:
    print("Aluno: {} | Média: {:.1f}".format(x["nome"], x["media"]))
