print("CONVERSÃO DE TEMPERATURAS")
cel = float(input("Informe a temperatura em °C: "))
F = (cel * 1.8) + 32
K = cel + 273.15

print("Fahrenheit: {:.2f}\nKelvin: {:.2f}".format(F, K))
