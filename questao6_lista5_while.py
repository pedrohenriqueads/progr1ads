#6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#Depois modique o programa para que ele mostre os números um ao lado do outro.
from time import sleep

#imprimindo um a baixo do outro
numero = 1
contador = 0

while contador < 20:
    print(numero)
    sleep(0.5)
    numero = numero + 1
    contador = contador + 1

#imprimindo um ao lado do outro
numero = 1
contador = 0

while contador < 20:
    print(numero, end=" " )
    sleep(0.5)
    numero = numero + 1
    contador = contador + 1

