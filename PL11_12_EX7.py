frases = []

while True:
    frase = input("Digite uma frase (Enter vazio para terminar): ")
    if frase == "": 
        break
    frases.append(frase)    

with open("user_text.txt", 'w') as file:
    file.write("\n".join(frases))

print("As frases foram guardadas com sucesso como user_text.txt")
