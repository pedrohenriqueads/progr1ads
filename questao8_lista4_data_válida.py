#8 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

ok_dia = False
ok_mes = False
ok_ano = False

if 1 <= dia <=31:
    ok_dia = True
if 1 <= mes <= 12:
    ok_mes = True
if 1900 <= ano <= 2100:
    ok_ano = True

if ok_dia and ok_mes and ok_ano:
    print("%d/%d/%d" % (dia,mes,ano))
    print("A data é válida")
else:
    print("%d/%d/%d" % (dia,mes,ano))
    print("Data inválida")
