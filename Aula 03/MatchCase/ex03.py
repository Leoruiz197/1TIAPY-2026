while True:
    opcao = int(input("Digite de 1 a 12 para escolher um mês e descobrir a estação correspondente: "))

    match opcao:
        case 12 | 1 | 2 : 
            print("Verão")
            break
        case 3 | 4 | 5 : 
            print("Outono")
            break
        case 6 | 7 | 8 :
            print("Inverno")
            break
        case 9 | 10 | 11 :
            print("Primavera")
            break
        case _ :
            print("Opção invalida, tente novamente")