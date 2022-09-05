
nota = int(input ('nota:'))
valido = 'sim'

while valido == 'sim':
    if nota >= 0 and nota <= 10:
        print ('Nota Valida')
        valido = 'sim'
    else:
        print ('Nota invalida!')
        valido = 'não'

print ('Fim do programa!')