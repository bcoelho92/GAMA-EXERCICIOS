print('Calculo de peso para Ele e para ela')

# Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('digite sua altura:'))

print('Peso ideal para homens:', round((72.7*h) - 58),2)
print('Peso ideal para mulheres:', round((62.1*h) - 44.7),2)

# round((62.1*h) - 44.7),2) - para arredondar os numeros reais 