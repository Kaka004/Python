# nome = 'Kayo'
# altura = 1.81
# peso = 105.0
# imc = peso / altura ** 2

# linha_1 = f'{nome} tem {altura} de altura'

# print(f"{nome} tem {altura} de altura.")
# print(f"Ele pesa {peso} kilos e seu IMC é {imc:.2f}")

# print('"ja sei"')

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')