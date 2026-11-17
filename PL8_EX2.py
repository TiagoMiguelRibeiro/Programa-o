x = float(input("Insere a distancia percorrida em km na 1 fase: "))
y = float(input("Insere a distancia percorrida em km na 2 fase: "))

total_time = 12 * x + 7 * y + 12 * (x + y)

print(f"Tempo total gasto na viagem: {total_time} minutos")
