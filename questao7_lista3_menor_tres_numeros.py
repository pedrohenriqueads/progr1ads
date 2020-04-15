#7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#Número maior

if n1 > n2 and n1 > n3:
    print ("O maior numero é:", n1)
elif n2 > n1 and n2 > n3:
    print ("O maior número é:", n2)
elif n3 > n1 and n3 > n2:
    print ("O maior número é:", n3)

elif n1 > n2 and n1 == n3:
    print ("O maior numero é:", n1)
elif n1 > n3 and n1 == n2:
    print ("O maior número é:", n1)
elif n2 > n1 and n2 == n3:
    print ("O maior número é:", n2)
elif n2 > n3 and n2 == n1:
    print ("O maior número é:", n2)
elif n3 > n1 and n3 == n2:
    print ("O maior número é:", n3)
elif n3 > n2 and n3 == n1:
    print ("O maior número é:", n3)

#Número iguais
    
elif n1 == n2 and n1 == n3:
    print("Os números são iguais")

#Número menor
    
if n1 < n2 and n1 < n3:
    print ("O menor numero é:", n1)
elif n2 < n1 and n2 < n3:
    print ("O menor número é:", n2)
elif n3 < n1 and n3 < n2:
    print ("O menor número é:", n3)

elif n1 < n2 and n1 == n3:
    print ("O menor numero é:", n1)
elif n1 < n3 and n1 == n2:
    print ("O menor número é:", n1)
elif n2 < n1 and n2 == n3:
    print ("O menor número é:", n2)
elif n2 < n3 and n2 == n1:
    print ("O menor número é:", n2)
elif n3 < n1 and n3 == n2:
    print ("O menor número é:", n3)
elif n3 < n2 and n3 == n1:
    print ("O menor número é:", n3)
    


