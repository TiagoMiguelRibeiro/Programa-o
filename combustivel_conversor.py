liters = float(input("Insere a quantidade de litros: "))
price_per_liter = 1.40
total = liters * price_per_liter

if liters > 40:
	total *= 0.90

print(f"Montante a pagar: {total:.2f}€")
