def find_median(lista):
    numeros = sorted(lista)

    n = len(numeros)

    for n in numeros:
        meio = n//2

        if n % 2 != 0:
            mediana = numeros[meio]

        else:

            mediana = (numeros[meio - 1 ] + numeros[meio]) / 2

    print(f"Mediana: {mediana}")


numbers = [3, 1, 4, 2] 

find_median(numbers)
