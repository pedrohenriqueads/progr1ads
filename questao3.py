#Questâo 3

km_inicial = int(input("Digite o km inicial: "))
km_final = int(input("Digite o km final: "))
km_total = km_final - km_inicial

print("quilometros pecorridos: %d Km" % km_total)

litros = float(input("Digite o total de litros gastos: "))
media = km_total / litros
print("O consumo médio é %.f litros" % media)
