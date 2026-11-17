P = 10000
n = 12
r = 0.08

t = float(input("Insere o numero de anos: "))
A =  P * (1 + r / n) ** (n * t)

print("Montante Final:", round(A, 2), "€")

