# Faça um Programa que leia três números e mostre o maior deles.

print ('='*20)
print ('O maior dos 3')
print ('='*20)

num1 = int(input('digite o 1º numero: '))
num2 = int(input('digite o 2º numero: '))
num3 = int(input('digite o 3º numero: '))
maior= num1
print ('')

if num2>num1 and num2>num3:
    maior = num2
    print('O 2º número é o maior: ', maior)
elif num3>num1 and num3>num2:
    maior = num3
    print('O 3º número é o maior: ', maior)

else: print('O 1º número é o maior: ', maior)

# validar logica 

print ('='*20)