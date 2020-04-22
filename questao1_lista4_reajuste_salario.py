
salario =float(input("Digite o salário: "))

if salario <= 280:
    salario_reaj = ((salario/100)*20) + salario
    porc = '20%'
    reajv = (salario/100)*20
elif salario > 280 and salario <= 700:
    salario_reaj = salario + (salario/100)*15
    porc = '15%'
    reajv = (salario/100)*15
elif salario > 700 and salario <= 1500:
    salario_reaj = salario + (salario/100)*10
    porc = '10%'
    reajv = (salario/100)*10
else:
    salario_reaj = salario + (salario/100)*5
    porc = '5%'
    reajv = (salario/100)*5

print("Salário antes do reajuste:", salario)
print("Salário reajustado:", salario_reaj)
print("Valor do reajuste:", reajv)
print("Porcentagem do reajuste:", porc)

