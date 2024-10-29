print("----- NOTAS DO ALUNO -----")
nome = print(input("Digite seu nome: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Agora, sua segunda nota: "))
total = nota1 + nota2 / 2

if(total < 5):
    print("Reprovado!")
else:
    print("Aprovado!")