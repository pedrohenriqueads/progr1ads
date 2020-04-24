#5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas decrescimento iniciais.
#Valide a entrada e permita repetir a operação.

popA = int(input('Digite a populaçao atual de A: '))
popB = int(input('Digite a populaçao atual de B: '))
anos = 0
cresA = float(input('Informe a taxa de porcentagem de crescimento de A: '))
cresB = float(input('Informe a taxa de porcentagem de crescimento de B: '))

while popA > popB:
    print('Operação inválida')
    popA = int(input('Digite a populaçao atual de A: '))
    popB = int(input('Digite a populaçao atual de B: '))
    anos = 0
    cresA = float(input('Informe a taxa de porcentagem de crescimento de A: '))
    cresB = float(input('Informe a taxa de porcentagem de crescimento de B: '))


while (popA < popB):
    anos += 1
    popA = popA + ((popA * cresA) /100)
    popB = popB + ((popB * cresB)/100)
print("Após %d anos o país A ultrapassou o país B em número de habitantes." % anos)

