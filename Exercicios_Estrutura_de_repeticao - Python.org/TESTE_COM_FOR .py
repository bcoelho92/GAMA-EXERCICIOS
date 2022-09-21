
print ('='*20)
print('''
Oi, vamos lá!

Vamos teste algo novo, :) o tal do FOR.

Vejamos como isso se repete ou não...

Vamos repetir o "OI" 3x.

''')

for C in range(0,3): # Python nao conta a ultima unidade.
    print('Oi!')
print('')

# Se quiser uma contagem tem que fazer o seguinte.

for C in range(0,6):  
    print(C) # Colocar o contador no lugar do "OI"
print('')

# Para uma contagem regrassiva 
for C in range(6,0, -1): # tem que inverter a ordem dos numeros e adicionar o "-1"
    print(C) # Colocar o contador no lugar do "OI"
print('')

# Contagem com intervalo 
for C in range(0,10,2):  # para contar com intervalo Basta adionar o numero do intervalo após a virgula ",2"
    print(C)
print('')


print('-Fim do programa-')
print('='*20)


