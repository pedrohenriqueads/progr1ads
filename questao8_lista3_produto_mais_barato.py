#8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 =float(input("Digite o preço do primeiro produto: "))
p2 =float(input("Digite o preço do segundo produto: "))
p3 =float(input("Digite o preço do terceiro produto: "))


if p1 < p2 and p1 < p3:
    print("O primeiro produto é o mais barato")
elif p2 < p1 and p2 < p3:
    print("O segundo produto é o mais barato")
elif p3 < p1 and p3 < p2:
    print("O terceiro produto é o mais barato")


elif p1 == p2 and p1 < p3:
    print("O primeiro e o segundo produto são os mais baratos")
elif p1 == p3 and p1 < p2:
    print("O primeiro e o terceiro produto são os mais baratos")
elif p2 == p3 and p2 < p1:
    print("O segundo e o terceiro produto são os mais baratos")



else:
    print("Todos os preços são iguais!")
