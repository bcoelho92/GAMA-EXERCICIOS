# Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
# M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Digite o seu turno, M-matutino ou V-Vespertino ou N- Noturno: '))

if turno.lower() == "m":
    print ('Bom dia!')
elif turno.lower() == "v":
    print ('Boa tarde!')
elif turno.lower() == "n":
    print ('Boa noite!')
else: print ('Valor Inválido!')

print('Fim do programa...')


# ******* VERIFICAR A CONDIÇÃO ABAIXO !!!!! ******* 

#if turno == "M"or"m":
#    print ('Bom dia!')
#elif turno == "V"or"v":
#    print ('Boa tarde!')
#elif turno == "N"or"n":
 #   print ('Boa noite!')
#else: print ('Valor Inválido!')
