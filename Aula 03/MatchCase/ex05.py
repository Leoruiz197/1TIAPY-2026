while True:
    nota = float(input("Digite sua nota para saber a classificação: "))

    match nota:
        case n if n > 10:
            print("Nota invalida, tente novamente!")
        case n if n >= 9:
            print("Excelente")
            break
        case n if n >= 7:
            print("Bom")
            break
        case n if n >= 5:
            print("Regular")
            break
        case n if n >= 0 :
            print("Reprovado")
            break
        case _ :
            print("Nota invalida, tente novamente!")