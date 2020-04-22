#5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
#O usuário deve informar o valor original da dívida (ex. R$ 50,00),
#a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

divida_original = float(input("Informe o valor original da divida: "))
dias_atraso = int(input("Informe os dias atrasados: "))
multa = float(input("informe o valor da multa: "))
valor_final = divida_original + dias_atraso * multa

print("O valor a ser pago é:", valor_final)
