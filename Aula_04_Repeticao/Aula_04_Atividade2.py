def se_erro(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("De novo... "))
    return nota

notaA = float(input("Digite a 1ª nota: "))
notaA = se_erro(notaA)

notaB = float(input("Digite a 2ª nota: "))
notaB = se_erro(notaB)

media = (notaA + notaB) / 2
print(media)