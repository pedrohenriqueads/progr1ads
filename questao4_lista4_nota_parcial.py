#4 -Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:
'''  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E 
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E.
'''

v1 =float(input("Digite o valor da primeira nota: "))
v2 =float(input("Digite o valor da segunda nota: "))
nota = (v1 + v2) /2

if nota >= 9 and nota <= 10:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um A!")
    print("Sua media é:", nota)
    print("Você foi Aprovado!!")

elif nota >= 7.5 and nota < 9:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um B!")
    print("Sua media é:", nota)
    print("Você foi Aprovado!!")

elif nota >= 6 and nota < 7.5:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um C!")
    print("Sua media é:", nota)
    print("Você foi Aprovado!!")

elif nota >= 4 and nota < 6:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um D!")
    print("Sua media é:", nota)
    print("Você foi Reprovado :(")

elif nota < 4:
    print("Nota da primeira prova:", v1)
    print("Nota da segunda prova:", v2)
    print("")
    print("Você tirou um E!")
    print("Sua media é:", nota)
    print("Você foi Reprovado :(")

    
