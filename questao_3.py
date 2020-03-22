#3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite (F)-Feminino, (M)-Masculino: ")
if sexo == 'f' or sexo == 'F':
    print("Feminino")
elif sexo == 'm' or sexo == 'M':
    print("Masculino")
else:
    print("Sexo invalido")
