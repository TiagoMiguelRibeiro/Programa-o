PF = 8.00
PC = 14.90
IMP = 0.23
TA = 0.10

quantidade = int(input("Número de t-shirts produzidas/vendidas: "))

# PC inclui IVA, por isso calcula-se o IVA correspondente ao preço bruto.
iva_unitario = PC * IMP / (1 + IMP)
iva_total = iva_unitario * quantidade
taxa_ambiental_total = TA * quantidade
taxas_totais = iva_total + taxa_ambiental_total
lucro_total = (PC - iva_unitario - PF - TA) * quantidade

print(f"Lucro total: {lucro_total:.2f}€")
print(f"IVA total: {iva_total:.2f}€")
print(f"Taxas totais (IVA e taxa ambiental): {taxas_totais:.2f}€")
