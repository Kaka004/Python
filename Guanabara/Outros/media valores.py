quantidade = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    quantidade = quantidade + 1
    valor = float(input("Digite um valor: "))
    
    media = soma / quantidade

print("\n Total da Soma: ", soma)
print("\n Quantidade de valores digitados: ", quantidade)
print("\n Média dos valores: ", media)