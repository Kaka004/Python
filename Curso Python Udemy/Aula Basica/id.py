"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""
# As duas variaveis apontam para o mesmo valor na memória
# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = False
passa_no_if = None

if condicao:
    passa_no_if = True
    print('Faça algo')
else:
    print('Não faça nada')
    
print(passa_no_if, passa_no_if is None)
print(passa_no_if, passa_no_if is not None)


if passa_no_if is None:
    print("Nao passou no if")
    
if passa_no_if is not None:
    print("Passou no if")