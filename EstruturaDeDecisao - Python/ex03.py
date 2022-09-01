# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


print ('='*20)
print ('POSITIVO OU NEGATIVO')
print ('='*20)

sexo = str(input('Digite "F" para feminino ou "M" para Masculino > '))
print ('')

if sexo == "F":
    print ('Seu Sexo é FEMININO!')
elif sexo == "M": print ('Seu sexo é MASCULINO!')
else: print('Sexo invalido!')

print ('='*20)