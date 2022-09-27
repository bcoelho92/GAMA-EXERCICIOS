# Nome
# Idade
# Filhos (incluindo os de estimação)
# Estado
# Altura
# Formação

# Calcule

# Dados Numéricos
    # A Moda
    # A Mediana
    # A média
    # Os Quartis
    # Os 10% maiores
    # Os 5 % Menores
    # O valor máximo
    # O valor mínimo

# Dados de Texto
    # A frequência absoluta
    # A frequência relativa
    # A Moda
    # Qual o tipo de Moda?
    # O valor máximo (ordem alfabética)
    # O valor mínimo (ordem alfabética)

import numpy as np
import pandas as pd

# arq = ('Exercicios_estatisticas\Exercicio_estatistica.csv') - abrir como variavel
df = pd.read_csv('Exercicios_estatisticas\Exercicio_estatistica.csv')
# print(df.info()) # INFORMAÇÕES DO DATA FRAME
# print(df.head(10)) # TOP10  DO DATA FRAME

df['Altura'] = df['Altura'].str.replace(',','.') # Troca de ',' por '.' .
df['Altura'] = df['Altura'].astype(float) # troca de typo da coluna.
# print(df['Altura'])

numericos  = ['Idade','Filhos','Altura']
'''
# Dados numericos 

moda = df[numericos].mode()
print(f'A Moda da idade, filhos e da Altura é \n {moda}\n')

mediana = df[numericos].median()
print (f'A mediana da idade, filhos e da Altura é \n {mediana}\n')

media = df[numericos].mean()
print (f'A média da idade, filhos e da Altura é \n {media}\n')  

q1 = df[numericos].quantile(.25)
print (f'Os Quartis da idade, filhos e da Altura é \n {q1}\n') 
q2 = df[numericos].quantile(.5)
print (f'Os Quartis da idade, filhos e da Altura é \n {q2}\n') 
q3 = df[numericos].quantile(.75)
print (f'Os Quartis da idade, filhos e da Altura é \n {q3}\n') 

top10 = df[numericos].sort_values().head(3).tolist()
print(f'Os 10% maiores: {top10}\n ')

dow5 = df[numericos].sort_values().tail(1).tolist()
print(f'Os 5 % Menores: {dow5}\n')

valmax = df[numericos].max()
print (f'O valor maximo da idade, filhos e da Altura é \n {valmax}\n') 

valmin = df[numericos].min()
print (f'O valor minimo da idade, filhos e da Altura é \n {valmin}\n') 
'''
# RESUMINDO TUDO ISSO:

print(df[numericos].describe(percentiles=[.05,.25,.5,.75,.9]))
print(df[numericos].mode())

df.to_csv('Exercicios_estatisticas\Exercicio_estatistica2.csv', index=False)

