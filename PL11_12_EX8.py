def analyse_file(file):
    file = open(file, 'r')
    conteudo = file.read()
    palavras = len(conteudo.split())
    caracteres = len(conteudo)
    print(f'O ficheiro tem {palavras} palavras e {caracteres} caracteres')

analyse_file("user_text.txt")

