"""
CONSTANTE => São "variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
        <= Contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local aonde o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o rada 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega

passouRadar = velocidade > RADAR_1
passouVelocidade = local_carro >= (LOCAL_1 - RADAR_RANGE) 
Km_carro = local_carro <= (LOCAL_1 + RADAR_RANGE)
carroMultado = passouVelocidade and passouRadar

if passouRadar:
    print("Você ultrapassou a velocidade permitida")
    
if passouVelocidade and Km_carro:
    print("Carro passou no radar")

if  carroMultado:
        print("Você foi multado!")