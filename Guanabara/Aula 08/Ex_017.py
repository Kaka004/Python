from math import hypot
print("---- CALCULANDO A HIPOTENUSA ----")
CO = float(input("Qual o valor do cateto oposto? "))
CA = float(input("Qual o valor do cateto adjacente? "))
hipo = hypot(CO, CA)
print("O valor da hipotenusa é {:.2f}".format(hipo))