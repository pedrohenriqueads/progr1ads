import math
print("Equaçao do 2° grau da forma: ax² + bx + c")
print("")    
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = b**2 - 4*a*c

if a == 0:
    print("É impossivel dividir por zero!")
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    print("A raiz desta equação é:",x1)
else:
    if delta < 0:
        print("Esta equação não possui raizes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("A primeira raiz é:", x1)
        print("A segunda raiz é:",x2)
