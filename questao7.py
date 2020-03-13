#Questão 7

print("Olá") #apresentação

largura1 = float(input("Digite a lagura do primeiro comodo: "))
comp1 = float(input("Digite o comprimento do primeiro comodo: "))
r1 = largura1 * comp1

largura2 = float(input("Digite a lagura do segundo comodo: "))
comp2 = float(input("Digite o comprimento do segundo comodo: "))
r2 = largura2 * comp2

largura3 = float(input("Digite a lagura do terceiro comodo: "))
comp3 = float(input("Digite o comprimento do terceiro comodo: "))
r3 = largura3 * comp3

largura4 = float(input("Digite a lagura do quarto comodo: "))
comp4 = float(input("Digite o comprimento do quarto comodo: "))
r4 = largura4 * comp4

print("O primeiro comodo mede %.2f ²" % r1)
print("O segundo comodo mede %.2f cm²" % r2)
print("O terceiro comodo mede %.2f cm²" % r3)
print("O quarto comodo mede %.2f cm²" % r4)

area_total = (largura1 + largura2 + largura3 + largura4) * (comp1 + comp2 + comp3 + comp4)
print("A area total da casa é %.2f cm²" % area_total)
