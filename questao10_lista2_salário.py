#10. Faça um programa que calcula o novo valor do salário de um funcionário.
#O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario  = float(input("Digite o salário:" ))
reajuste  = float(input("Digite uma porcentagem do aumento:" ))

novoSalario  =  salario  + (( salario * reajuste ) / 100 )
aumento  =  novoSalario  -  salario

print("Aumento de %.2f $" % aumento)

print("Novo salário %2.f $" % novoSalario)
