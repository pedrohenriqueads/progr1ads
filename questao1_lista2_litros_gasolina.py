#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75)
#e quanto em dinheiro ele deseja abastecer (ex. 50,00).
#Calcule quantos litros de combustível o usuário obterá com esses valores.


valor_litro = float(input("Digite o valor do combustivel: "))
valor_abastecido = float(input("digite o valor em dinheiro que deseja absatecer: "))
litros = valor_abastecido / valor_litro 
print("Você abasteceu %.2f litros" % litros)
