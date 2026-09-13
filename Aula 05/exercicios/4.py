# with open('meuarquivo3.txt','r',encoding = "utf-8") as file:
#     linhas = file.readlines()
#     linhas.sort()    

# with open('ordenado.txt','w',encoding = "utf-8") as file:
#     for linha in linhas:
#         file.write(linha)

lista_ordenada = []

with open('meuarquivo3.txt','r',encoding = "utf-8") as file:
    linhas = file.readlines()
    lista_ordenada = sorted(linhas)   

with open('ordenado.txt','w',encoding = "utf-8") as file:
    for linha in lista_ordenada:
        file.write(linha)