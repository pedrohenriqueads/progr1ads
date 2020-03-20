lado1 = input("Digite o valor do primeiro lado: ")
lado2 = input("Digite o valor do segundo lado: ")
lado3 = input("Digite o valor do terceiro lado: ")

if lado1 + lado2 > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Triângulo Isósceles")
    elif lado1 != lado2 and lado1 != lado3 or lado2 != lado1 and lado2 != lado3 or lado3 != lado1 and lado3 != lado2:
        print("Triângulo Escaleno")

else:
    print("Não é um triângulo")
