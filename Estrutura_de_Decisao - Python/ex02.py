# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print ('='*20)
print ('POSITIVO OU NEGATIVO')
print ('='*20)

numero1 = int(input('digite um numero: '))

if numero1 >= 0 :
     print ('O numero',numero1,'é POSITIVO!')
else:
     print ('O numero ',numero1, 'é NEGATIVO!')

# forma mais limpa 
# print ('positivo' if numero > o else 'negativo')