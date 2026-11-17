sentence = input("Escreve a frase: ")


def reverse_words(sentence):
    palavras = sentence.split()
    frase_nova = " ".join(palavra[::-1] for palavra in palavras)
    print(frase_nova)


reverse_words(sentence)
