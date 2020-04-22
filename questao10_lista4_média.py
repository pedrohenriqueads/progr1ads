nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma = (nota1 + nota2) /2
if soma >= 7 and soma < 10:
    print("Aprovado")
elif soma == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")
    
if soma <= 10:
    media = int(input("Deseja ver a média? (1)-Sim (2)-Não: "))
    if media == 1:
        print("Sua média é:", soma)
    elif media == 2:
        print("programa encerrado")
    else:
        print("Error")
else:
    print("Ops, operação inválida")

