import math

num = int(input("Insere um número: "))

if num <100 or num > 999:
    print("O numero nao tem 3 digitos")

else:

    d3 = num % 10
    d2 = (num // 10) % 10
    d1 = (num // 100) % 10
    
    print(f"{d1}, {d2}, {d3}")

