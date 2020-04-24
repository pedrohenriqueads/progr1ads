#9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

#numéros ímpares 
num = 0
cont = 0
while cont < 50:
    num = num + 1
    if num % 2 != 0:
        print(num, end=' ')
    cont = cont + 1
print("")

#números pares
num = 0
cont = 0
while cont <= 50:
    num = num + 1
    if num % 2 == 0:
        print(num, end=' ')
    cont = cont + 1
print('FIM')
