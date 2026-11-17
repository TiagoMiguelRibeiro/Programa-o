frase = str(input("Digite uma frase: "))
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

vowel = sum(1 for char in frase if char in vogais)

if vowel > 0:
    frase_sem_vogais = frase
    for vogal in vogais:
        frase_sem_vogais = frase_sem_vogais.replace(vogal, "*") 
    print("Frase com vogais substituídas por '*':", frase_sem_vogais)

def word_count(frase):
    palavras = frase.split()
    return len(palavras)

unique_words = set(frase.split())

print("Número de palavras na frase:", word_count(frase))
print("Número de palavras únicas na frase:", len(unique_words))