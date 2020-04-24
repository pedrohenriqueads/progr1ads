#4- Suponha que a população de um país A seja da ordem de 80.000 habitantes com umataxa anual de crescimento de 3%
#e que a população de B seja 200.000 habitantes com uma taxade crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários
#para que a população do país A ultrapasse ou iguale a população do país B,mantidas as taxas de crescimento.

popA = 80000
popB = 200000
anos = 0
cresA = 0.03 
cresB = 0.15
while (popA < popB):
    anos += 1
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)
print("Após %d anos o país A ultrapassou o país B em número de habitantes." % anos)
