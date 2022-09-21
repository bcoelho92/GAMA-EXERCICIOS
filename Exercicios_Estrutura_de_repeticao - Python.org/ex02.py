# tabuada

print('')
print('')
print('')

numero = -1

# numero = int(input('Digite um numero: '))

while numero < 0 or numero > 10: # condição de loop
    numero = int(input('Digite um numero valido: ')) # condição de loop
    
    if numero >= 0 and 10 <= numero:
        print ('numero valido')
    else:
        print('Numero invalido, digite um valor entre 0 e 10.')



print ('')
print ('Fim do programa')