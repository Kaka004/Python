from math import sin, cos, tan, radians

angulo = float(input("Informe o valor do Angulo: "))
rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print("--- VALORES ---\n")
print(f"Seno de {angulo}°: {seno:.2f}")
print(f"Cosseno de {angulo}°: {cosseno:.2f}")
print(f"Tangente de {angulo}°: {tangente:.2f}")
