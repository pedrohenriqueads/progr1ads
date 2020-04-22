v1 =float(input("Digite o valor da primeira nota: "))
v2 =float(input("Digite o valor da segunda nota: "))
nota = (v1 + v2) /2

if nota >= 9 and nota <= 10:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um A!")
    print("Sua media é:", nota)
    print("Você foi Aprovado!!")

elif nota >= 7.5 and nota < 9:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um B!")
    print("Sua media é:", nota)
    print("Você foi Aprovado!!")

elif nota >= 6 and nota < 7.5:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um C!")
    print("Sua media é:", nota)
    print("Você foi Aprovado!!")

elif nota >= 4 and nota < 6:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um D!")
    print("Sua media é:", nota)
    print("Você foi Reprovado :(")

elif nota < 4:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um E!")
    print("Sua media é:", nota)
    print("Você foi Reprovado :(")

    
