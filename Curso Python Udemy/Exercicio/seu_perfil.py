"""
Peça ao usuário para digitar:
-Nome;
-Idade;
Se nome e idade forem digitados:
    Exiba:
    - Nome
    - Nome invertido
    - Se contem ou nao espaços
    - Quantas letras tem seu nome
    - A primeira do seu nome
    - A ultima letra do seu nome
    Se nada for digitado em nome ou idade:
    - Exiba (Desculpe, você deixou campos vazios)
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
spaces = nome.count(" ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome ivertido é " + nome[-1:-5:-1])
    if '' and nome:
        print("Seu nome tem espaços")
    else:
        print("Seu nome não tem espaços")
    
    print(f"Seu nome tem {len(nome)} letras")
    print("Primeira letra do seu nome: " + nome[0])
    print("Última letra do seu nome: " + nome[-1])
else: 
    print("Desculpe, você deixou campos vazios")
