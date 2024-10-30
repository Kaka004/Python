"""
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""
#O input sempre vai retornar uma string
# num = input("Coloque um numero para a dobra: ")

# #Caso for digitar um numero, por exemplo 5, irá
# #retornar 55
# result = print(f"O dobro de {num} é {num * 2}")
# ================================================
#Para que o numero que digitou, retorne o dobro, ele
#prescisa ser int ou float
num = input("Coloque um numero para a dobra: ") # retorna uma string
#num = int(num) agora virou inteiro
 
#Check se o usuário digitou apenas numeros
try: 
    num_float = float(num)
    print('Float:', num_float)
    print(f"O dobro de {num} é {num_float * 2:.1f}")
except:
    print('Isso não é um numero!')


# if num.isdigit():
#     num = float(num) # agora virou float
#     print(f"O dobro de {num} é {num * 2}")
# else:
#     print("Isso não é um número")

