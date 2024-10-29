num = input("Digite um número: ")

if not num.isdigit():
    print("Esse número não é inteiro")
else:
    num_int = int(num)
    if num % 2 == 0:
        print("Esse número é par")
    else:
        print(f"O número {num_int} é impar")