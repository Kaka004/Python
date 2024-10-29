print("--- PREÇO COM 5% DE DESCONTO")
preco = float(input("Digite a valor do produto: "))
desconto = preco * 0.05
valor = preco - desconto
print("O valor agora será: R${:.2f}".format(valor))
