idade = int(input("Digite sua idade: "))

match idade:
    case i if i > 17:
        print("Adulto")
    case i if i > 12:
        print("Adolescente")
    case i if i > -1:
        print("Criança")
    case _ :
        print("Idade invalida!")