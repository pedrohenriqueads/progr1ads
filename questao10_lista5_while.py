#10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Dgite um número inteiro: '))
num2 = int(input('Dgite um número inteiro: '))

while num1 < num2:
    num1 = num1 + 1
    if num1 < num2:
        print(num1)
   
while num2 < num1:
    num2 = num2 +1
    if num2 < num1:
        print(num2)
    
