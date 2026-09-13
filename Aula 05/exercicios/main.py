arquivo = input("Digite o nome do arquivo: ")
arquivo2 = input("Digite o nome do segundo arquivo: ")

conteudo = ""
conteudo2 = ""

with open(arquivo, "r", encoding="UTF-8") as file:
    conteudo = file.read()

with open(arquivo2, "r", encoding="UTF-8") as file:
    conteudo2 = file.read()

with open("teste.txt","w", encoding="UTF-8") as file:
    file.write(conteudo)
    file.write(conteudo2)