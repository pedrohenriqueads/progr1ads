#5 - Receba do usuário o ano em que estamos, e o ano que ele nasceu, e calcule sua idade. Despreze os meses.

ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano em que nasceu: "))
idade = ano_atual - ano_nasc
print("Sua idade é:", idade)
