import random

print("---- SORTEIO DE ALUNOS ----")

aluno1 = "Maria"
aluno2 = "Marcos"
aluno3 = "Davi"
aluno4 = "Giovana"

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

print("Ordem dos alunos sorteados:")

for i, aluno in enumerate(alunos, 1):
    print(f"{i}. {aluno}")
