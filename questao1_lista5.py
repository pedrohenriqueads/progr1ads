#1 - Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem casoo valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite uma nota entre 0 e 10:"))

while nota >10 :
    nota = int(input("Digite uma nota entre 0 e 10:"))
print(nota)
    
    
