
valor_hora = float(input("Digite o valor da hora de trabalho: "))
total_hora_trabalhada = float(input("Digite a quantidade de hora trabalhada no mês: "))
salario_bruto = (valor_hora*total_hora_trabalhada)
desc_sindicato = (salario_bruto/100)*3
fgts = (salario_bruto/100)*11
ir = 0

if salario_bruto <= 900:
    salario_liquido = salario_bruto - desc_sindicato
        
elif salario_bruto <= 1500:
    ir = (salario_bruto/100)*5
    salario_liquido = salario_bruto - desc_sindicato - ir
        
elif salario_bruto <= 2500:
    ir = (salario_bruto/100)*10
    salario_liquido = salario_bruto - desc_sindicato - ir
        
else:
    ir = (salario_bruto/100)*20
    salario_liquido = salario_bruto - desc_sindicato - ir

print("Salario Bruto: %.2f" % salario_bruto)
print("Desconto Sindicato: %.2f" % desc_sindicato)
print("Desconto IR: %.2f" % ir)
print("FGTS: %.2f" % fgts)
print("Salario Liquido: %.2f" % salario_liquido)
    
