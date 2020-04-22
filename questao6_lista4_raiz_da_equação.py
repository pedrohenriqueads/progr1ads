#6 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

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
