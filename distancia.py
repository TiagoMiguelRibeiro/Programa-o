import math

x1 = int(input("Insere a coordenada x1: "))
y1 = int(input("Insere a coordenada y1: "))
x2 = int(input("Insere a coordenada x2: "))
y2 = int(input("Insere a coordenada y2: "))

distancia = math.hypot(x2 - x1, y2 - y1)
print(f"A distância entre os pontos é: {distancia}")