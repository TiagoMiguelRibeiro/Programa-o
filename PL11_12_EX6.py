sentence = str(input("Escreve a frase: "))

frase_nova = ""

def reverse_words(sentence):
    for palavra in sentence:

        palavra = sentence.split()

        for letras in palavra:

            frase_nova = palavra[::-1]

    print(frase_nova)

reverse_words(sentence)