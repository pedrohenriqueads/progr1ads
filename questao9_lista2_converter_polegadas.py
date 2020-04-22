#9. Escreva um programa que converte valores de polegadas em centímetros
#utilizando a seguinte fórmula para conversão: 1 polegada = 2,54 cm;

polegada = float(input("Digite o valor em polegadas: "))
resultado = polegada * 2.54

print("O valor convertido é %.2f cm" % resultado)
