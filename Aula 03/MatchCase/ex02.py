while True:
    opcao = int(input("Digite de 1 a 7 para selecionar o dia: "))

    match opcao:
        case 1 : 
            print("Segunda-Feira")
            break
        case 2 : 
            print("Terça-Feira")
            break
        case 3 :
            print("Quarta-Feira")
            break
        case 4 :
            print("Quinta-Feira")
            break
        case 5 :
            print("Sexta-Feira")
            break
        case 6 :
            print("Sabado")
            break
        case 7 :
            print("Domingo")
            break
        case _ :
            print("Opção invalida, tente novamente")