with open('meuarquivo.txt','r',encoding = "utf-8") as file:
    conteudo = file.read()
    palavras = conteudo.split()
    print(len(palavras))