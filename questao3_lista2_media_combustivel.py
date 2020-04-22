#3. Faça um programa que calcule a média de consumo de combustível de um veículo.
#O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km_inicial = int(input("Digite o km inicial: "))
km_final = int(input("Digite o km final: "))
km_total = km_final - km_inicial

print("quilometros pecorridos: %d Km" % km_total)

litros = float(input("Digite o total de litros gastos: "))
media = km_total / litros
print("O consumo médio é %.f litros" % media)
