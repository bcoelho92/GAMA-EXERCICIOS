# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# ada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 
# R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print ('='*20)
print ('')
print ('='*20)

import math

print('='*14)
print('Loja de Tintas')
print('='*14)
print()

area = float(input('Área a ser pintada (m²): '))
litros = area/6
litros_folga = litros + litros*.10
latao = litros_folga//18
latinhas = (litros_folga - 18*latao)/3.6
latinhas_arredondado = math.ceil(latinhas)
preco = latao*80 + latinhas_arredondado*25

print('a) comprar apenas latas de 18 litros: ', math.ceil(litros/18))
print('b) comprar apenas galões de 3,6 litros: ', math.ceil(litros/3.6))
print('c) comprar latas e galões:')
print('   Latas: ', latao)
print('   Galões: ', latinhas_arredondado)
print('='*14)