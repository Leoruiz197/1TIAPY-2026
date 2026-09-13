texto1 = ""
texto2 = ""

with open('meuarquivo.txt','r',encoding = "utf-8") as file:
    texto1 = file.read()

with open('meuarquivo2.txt','r',encoding = "utf-8") as file:
    texto2 = file.read()

with open('meuarquivo3.txt','w',encoding = "utf-8") as file:
    file.write(texto1)
    file.write(texto2)