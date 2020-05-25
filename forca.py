import os

palavra = []
resposta = []
palavra_secreta = input('Digite a palavra secreta: ')
os.system('cls')
palavra.extend(palavra_secreta)
resposta.extend('_' * len(palavra_secreta))

for indice in resposta:
    print(indice, end=' ')
print('\n')

erros = 0
acertou = False

while erros < 6 and not acertou:
    letras = input('Arrisque uma letra: ')
    if letras in palavra:
        for indice in range(len(palavra)):
            if letras.upper() == palavra[indice].upper():
                resposta[indice] = letras
                if resposta == palavra:
                    acertou = True
        print(''.join(resposta))

    else:
        print('A palavra secreta não contem essa letra')
        erros = erros + 1

if acertou:
    print('')
    print('Parabéns você ganhou!!')
else:
    print('')
    print('Que pena você perdeu!!')
