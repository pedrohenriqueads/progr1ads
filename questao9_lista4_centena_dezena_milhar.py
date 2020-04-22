

n = int(input("Digite o número de teste: "))

if n > 1000:
    centena = n // 100 % 10
    dezena = n // 10 % 10
    unidade = n % 10
    if centena > 1 and dezena >1 and unidade >1:
         print( "%d centenas, %d dezenas e %d unidades" %( centena, dezena, unidade))
    elif centena > 1 and dezena > 1 and unidade < 2:
        print("%d centenas, %d dezenas e %d unidade" % (centena, dezena, unidade))
    elif centena > 1 and  dezena < 2 and unidade < 2:
        print("%d centenas, %d dezena e %d unidade" % (centena, dezena, unidade))
    elif centena < 2 and dezena < 2 and unidade < 2:
        print("%d centena, %d dezena e %d unidade" % (centena, dezena, unidade))
    elif centena < 2 and dezena < 2 and unidade > 1:
        print("%d centena, %d dezena e %d unidades" % (centena, dezena, unidade))
    elif centena < 2 and dezena > 1 and unidade > 1:
        print("%d centena, %d dezenas e %d unidades" % (centena, dezena, unidade))