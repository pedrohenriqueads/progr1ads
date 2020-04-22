'''1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-- salários até R$ 280,00 (incluindo) : aumento de 20%
-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-- o salário antes do reajuste;
-- o percentual de aumento aplicado;
-- o valor do aumento;
-- o novo salário, após o aumento.'''

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

