# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


print ('='*20)
print ('POSITIVO OU NEGATIVO')
print ('='*20)

sexo = str(input('Digite "F" para feminino ou "M" para Masculino > '))
print ('')

if sexo.lower() == "f":
    print ('Seu Sexo é FEMININO!')
elif sexo.lower() == "m": print ('Seu sexo é MASCULINO!')
else: print('Sexo invalido!')

print ('='*20)

# Convert letra para minusculo / elif - sexo.lower() == "m":- 
