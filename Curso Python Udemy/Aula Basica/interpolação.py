"""
Interpolação Básica de Strings
%s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)    
"""

nome = 'Kayo'
preco = 1000.95897643
variavel = '%s, o preço é de R$%.2f ' % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %04x" % (1500, 1500))