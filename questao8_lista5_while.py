#8 - Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 0
soma = 0
media = 0
while cont < 5:
    num = int(input('Informe um número: '))
    soma = soma + num
    media = soma / 5
    cont = cont +1
print('A soma é:',soma)
print('A média é:',media)
