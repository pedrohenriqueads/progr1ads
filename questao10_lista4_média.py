#10 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#- A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma = (nota1 + nota2) /2
if soma >= 7 and soma < 10:
    print("Aprovado")
elif soma == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")
    
if soma <= 10:
    media = int(input("Deseja ver a média? (1)-Sim (2)-Não: "))
    if media == 1:
        print("Sua média é:", soma)
    elif media == 2:
        print("programa encerrado")
    else:
        print("Error")
else:
    print("Ops, operação inválida")

