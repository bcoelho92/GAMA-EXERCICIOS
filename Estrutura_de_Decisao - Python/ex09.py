# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 =int(input('Digite o 1º numero: '))
n2 =int(input('Digite o 2º numero: '))
n3 =int(input('Digite o 3º numero: '))
p = 0

print ('')

if n1>n3 :
    p=n1
    n1=n3
    n3=p

if n1>n2:
    p=n1
    n1=n2
    n2=p

if n2>n3:
    p=n2
    n2=n3
    n3=p

print ('A ordem é :', n1,n2,n3)
print ('')
print ('Fim do programa.')
