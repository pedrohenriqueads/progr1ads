#7- Faça um programa que leia 5 números e informe o maior número.
cont = 0
maior = -0 
while cont < 5:
    num = int(input('Informe um número: '))
    if num > maior:
        maior = num
    cont = cont +1
print(maior)
