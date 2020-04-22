#4. Escreva um programa que leia uma temperatura em graus Fahrenheit,
#transforme-a em graus Celsius e exiba o resultado.

temp_f = float(input("Digite a temperatura em fahrenheit: "))
celsius = 5 * (temp_f - 32) / 9
print("A temperatura em celsius é %.2f graus" % celsius)

#convertendo para fahrenheit

temp_c = float(input("Digite a temperatura em celsius: "))
fahrenheit = temp_c * (9 / 5) + 32
print("A temperatura em fahrenheit é %.2f graus" % fahrenheit)

