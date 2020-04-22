#Questâo 5

divida_original = float(input("Informe o valor original da divida: "))
dias_atraso = int(input("Informe os dias atrasados: "))
multa = float(input("informe o valor da multa: "))
valor_final = divida_original + dias_atraso * multa

print("O valor a ser pago é:", valor_final)
