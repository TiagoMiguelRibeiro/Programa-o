dollars = float(input("Insira o valor em dólares: "))

preço_dollar = 1.17

euros = float(dollars / preço_dollar) # Assuming 1 Dollar = 1.17 Euros

print(f"O valor em euros é: {round(euros, 2)} €")