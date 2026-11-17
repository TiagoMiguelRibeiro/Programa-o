diametro = int(input("Insere o diametro da laranja em cm: "))

V = (4/3) * 3.14 * (diametro / 2) ** 3

if V <= 120:
    print("Sem classificação")

elif V > 120 and V <= 250:
    print("Classificação 1")

elif V > 250 and V <= 550:
    print("Classificação 2")

elif V > 550:
    print("Sem classificação - Está acima do tamanho máximo permitido")