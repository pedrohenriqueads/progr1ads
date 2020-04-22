#9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#- 326 = 3 centenas, 2 dezenas e 6 unidades
#- 12 = 1 dezena e 2 unidades 
#- Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


numero = int(input("Informe um numero para decompor: "))
if 0 < numero < 1000:
	centena = numero // 100 % 10
	dezena = numero // 10 % 10
	unidade = numero % 10
	tx_c = tx_d = tx_u = ""
	if centena >= 2:
		tx_c = "centenas"
		if dezena >= 2:
			tx_d = "dezenas"
			if unidade >= 2:
				tx_u = "unidades"
			else:
				tx_u = "unidade"
		else:
			tx_d = "dezena"
			if unidade >= 2:
				tx_u = "unidades"
			else:
				tx_u = "unidade"
	else:
		tx_c = "centena"
		if dezena >= 2:
			tx_d = "dezenas"
			if unidade >= 2:
				tx_u = "unidades"
			else:
				tx_u = "unidade"
		else: 
			tx_d = "dezena"
			if unidade >= 2:
				tx_u = "unidades"
			else:
				tx_u = "unidade"
	if centena > 0:
		print("%d %s, %d %s e %d %s" % (centena, tx_c, dezena, tx_d, unidade, tx_u))
	elif dezena > 0:
		print("%d %s e %d %s" % (dezena, tx_d, unidade, tx_u))
	elif unidade > 0:
		print("%d %s" % (unidade, tx_u))
