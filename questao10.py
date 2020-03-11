#Questão 10

salario  = float(input("Digite o salário:" ))
reajuste  = float(input("Digite uma porcentagem do aumento:" ))

novoSalario  =  salario  + (( salario * reajuste ) / 100 )
aumento  =  novoSalario  -  salario

print("Aumento de %.2f $" % aumento)
print("Novo salário %2.f $" % novoSalario)
