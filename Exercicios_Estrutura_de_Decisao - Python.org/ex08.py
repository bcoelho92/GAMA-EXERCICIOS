#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

print ('='*20)
print ('O mais barato!')
print ('='*20)

prod1 = float(input('Digite o valor do 1º produto R$: '))
prod2 = float(input('Digite o valor do 2º produto R$: '))
prod3 = float(input('Digite o valor do 3º produto R$: '))

menor = prod1 

print ('')

if prod2<prod1 and prod2<prod3:
    menor = prod2
    print('Comprar o 2º produto ele é o mais barato, custa R$', menor)
elif prod3<prod1 and prod3<prod2:
    menor = prod3
    print('Comprar o 3º produto ele é o mais barato, custa R$', menor)

elif menor :
    print ('compre o 1º produto ele é mais barato, custa R$', menor)
    
print ('='*20)

# if prod1 < prod2 and prod3:
#     print('Compre o 1º produto ele é o mais barato, valor: R$', prod1)
# elif prod2 < prod1 and prod3:
#     print('Compre o 2º produto ele é o mais barato, valor: R$', prod2)
# elif prod3 < prod2 and prod1:
#     print('Compre o 3º produto ele é o mais barato, valor: R$', prod3)