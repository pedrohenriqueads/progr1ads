#10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite seu turno: M-matutino ou V-Vespertino ou N- Noturno: ')

if turno == 'M':    
    print("Bom dia")        
elif turno == 'V': 
    print("Boa tarde")        
elif turno == 'N': 
    print("Boa Noite")        
else:    
    print("Vslor invalido")
