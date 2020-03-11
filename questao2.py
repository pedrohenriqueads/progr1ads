#Questão 2
#5 minutos banho = 45 litros
#1m³ = 1000 litros
#quantos banhos de 5 minutos consomem 1 metro cubico de água?
minutos_banho = 5
agua_banho = 45
total_litros = 1000
soma = total_litros / agua_banho
print("Em um banho de 5 minutos, 1m3 litros, permite que você tome %.f banhos" % soma)

# acrescimo de questao

tempo_banho = int(input("Diga quantos minutos você passa no banho: "))
litros_minutos = 9
gasto_no_banho = tempo_banho * litros_minutos
quantidade_banho = 1000 / gasto_no_banho
print("Para um banho de %d minutos, 1m3 permite %d banhos" % (tempo_banho, quantidade_banho))
