
# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#  e que a tinta é vendida em latas de 18 litros,
#  que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.

import math
math.ceil

print ('='*20)
print ('    Loja de tintas')
print ('='*20)

tmetrosq = float(input('Informe metros quadados ')) # metros quadrados 
litro = tmetrosq / 3 # litros de tinta 
qlatas = litro / 18 # quantidade latas de tinta
valorlata = qlatas * 80,00,35 # valor gasto com latas 

print ('A Quantidades de latas que você deve comprar é', qlatas, 2)
print ('Com o custo total de R$', valorlata)
