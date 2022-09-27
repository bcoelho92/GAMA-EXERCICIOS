import numpy as np
import pandas as pd

print()

# Dados de Texto

    # A frequência absoluta
    # A frequência relativa
    # A Moda
    # Qual o tipo de Moda?
    # O valor máximo (ordem alfabética)
    # O valor mínimo (ordem alfabética)

df = pd.read_csv('Exercicios_estatisticas\Exercicio_estatistica2.csv')
df["Estado"] = df["Estado"].str.upper()
df["Estado"] = df["Estado"].str.strip()
df['Nome'] = df['Nome'].str.title()
df['Nome'] = df['Nome'].str.strip()
df['Formação'] = df['Formação'].str.title()
df['Formação'] = df['Formação'].str.strip()
textos = ['Nome','Estado','Formação']
# print(df.info())

# Dados de Texto    

def tipo_moda(serie):
    qtd = len(serie.mode()) #.shape
    if qtd == 0:
        return 'Sem Moda'
    elif qtd == 1:
        return 'Unimodal'
    elif qtd == 2:
        return 'Bimodal'
    elif qtd > 2:
        return 'Multimodal'
    else:
        return 'Valor inválido'

print()
print('TRATAMENTO DE TEXTO !')
print()

for col in textos:
    df[col] = df[col].str.lower() # passa tudo para minúsculo
    df[col] = df[col].str.strip() # remove espaços em branco no começo ou final
    print()
    print(col)
    print(f'Frequência Absoluta: ')
    print(f'{df[col].value_counts()}')
    print()
    print(f'Frequência Relativa: ')
    print(f'{df[col].value_counts(normalize=True)}')
    print()
    print(f'Moda: {df[col].mode()[0]}')
    print(f'Mínimo: {df[col].min()}')
    print(f'Máximo: {df[col].max()}')
    print(f'Tipo de Moda: {tipo_moda(df[col])}')


# df.to_csv('Exercicios_estatisticas\Exercicio_estatistica3.csv', index=False)