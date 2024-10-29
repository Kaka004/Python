def LerNotas():
    nota = float(input("Digite sua nota: "))
    return nota

def Resultado(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4 ) / 4
    print ("Nota 1: ", n1)
    print ("Nota 2: ", n2)
    print ("Nota 3: ", n3)
    print ("Nota 4: ", n4)
    print("Media: ", media, "\n Resultado: ", end="")
    
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
        
A = LerNotas()
B = LerNotas()
C = LerNotas()
D = LerNotas()
Resultado(A, B, C, D)