print("========= menu =========")
print(" 1 - Ver perfil")
print(" 2 - Editar Perfil")
print(" 3 - Sair")

while True:
    opcao = int(input("Selecione uma das opções acima: "))

    match opcao:
        case 1 : 
            print("Visualizando o perfil")
            break
        case 2 : 
            print("Editando o perfil")
            break
        case 3 :
            print("Saindo...")
            break
        case _ :
            print("Opção invalida, tente novamente")