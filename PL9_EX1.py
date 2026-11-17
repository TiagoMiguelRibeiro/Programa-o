dia_inicio = int(input("Introduza o número do dia de partida (0 a 6): "))
numero_noites = int(input("Introduza o número de noites da estadia: "))

dia_regresso = (dia_inicio + numero_noites) % 7
print("O número do dia de regresso é:", dia_regresso)

if dia_regresso == 0:
    print("O dia de regresso é domingo.")

elif dia_regresso == 1:
    print("O dia de regresso é segunda-feira.")

elif dia_regresso == 2:
    print("O dia de regresso é terça-feira.")

elif dia_regresso == 3:
    print("O dia de regresso é quarta-feira.")

elif dia_regresso == 4:
     print("O dia de regresso é quinta-feira.")

elif dia_regresso == 5:
    print("O dia de regresso é sexta-feira.")

else:
    print("O dia de regresso é sábado.")
