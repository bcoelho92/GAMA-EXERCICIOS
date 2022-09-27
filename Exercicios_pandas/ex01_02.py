# 1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
#    1. Idade: números inteiros aleatórios entre 0 e 100 (inclusos).
#    2. Nota: Números decimais entre 0 e 1000.
#    3. Sexo: Valores aleatórios de M ou F
#    4. Estado: Valores aleatórios entre os estados do Brasil.

# 2. Utilizando pandas, realize as seguintes alterações no dataset:
#    1. Transforme 20% das notas em valores nulos(None), simulando alunos que não compareceram à prova.
#    2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
#      `df = df.fillna(0)`
#    3. Remova alunos com idades inferiores a 18 e superiores a 80, simulando uma filtragem automática do sistema para alunos com idades incosistentes.
#    4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior a 600, com o valor 'Aprovado'. Simulando uma correção automática.
#    5. Preencha o resto do campo de aprovado com 'Reprovado' para os demais alunos (preenchimento de nulo).
#    `df = df[coluna].fillna('Reprovado')`
#    6. Mostre a quantidade de alunos aprovados e reprovados.

print()
import sys
import numpy as np
import pandas as pd

#### DECLARAÇÃO DOS FRAMES 

idade = np.random.randint(low=0, high=101, size=[1000])
# print(idade)
# print()

notas = np.random.uniform(low=0, high=1000, size=[1000])  
# print(notas)
# print()

opcoes = ['F', 'M']
genero =  np.random.choice(opcoes, size=[1000])
# print(genero)
# print()

opcoes1 = ['AC','AL','AP',
            'AM','BA','CE',
            'ES','GO','MA',
            'MT','MS','MG',
            'PA','PB','PR',
            'PE','PI','RJ',
            'RN','RS','RO',
            'RR','SC','SP',
            'SE','TO','DF']

estado = np.random.choice(opcoes1, size=[1000])
# print(estado)
# print()

# tamanho das listas/frame
# print(len(estado),len(genero),len(notas),len(idade))

### Criação da séries

idade = pd.Series(idade, name='Idade')
notas = pd.Series(notas,name='Notas')
genero = pd.Series(genero, name='Genero')
estado = pd.Series(estado,name='Estado')

### Transforma em DataFrame

turma1 = pd.DataFrame({
    'Idade':idade,
    'Notas':notas,
    'Genero':genero,
    'Estado':estado,
})

turma1.to_csv('Exercicios_pandas/notasdaturma1.csv', index=False)

# 1. Transforme 20% das notas em valores nulos(None), simulando alunos que não compareceram à prova.
alunos_faltantes = turma1.sample(frac=.2, random_state=0).index
turma1.loc[alunos_faltantes, 'nota'] = None

# 2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
turma1 = turma1.fillna(0)

 # 3. Remova alunos com idades inferiores a 18 e superiores a 80, simulando uma filtragem automática do sistema para alunos com idades incosistentes.
menor_18 = turma1['Idade'] < 18 
maior_80 = turma1['Idade'] > 80 #>18 & <80
filtro = ~(menor_18 | maior_80) 
#[index, coluna]
turma1 = turma1.loc[filtro, :]
print(turma1.loc[filtro, :])

# 4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior a 600, com o valor 'Aprovado'. Simulando uma correção automática.
maior_600 = turma1['Notas'] > 600
turma1['aprovado'] = None
turma1.loc[maior_600, 'aprovado'] = 'Aprovado'
print(turma1)

# 5. Preencha o resto do campo de aprovado com 'Reprovado' para os demais alunos (preenchimento de nulo).
turma1['aprovado'] = turma1['aprovado'].fillna('Reprovado')
#df.loc[~maior_600, 'aprovado'] = 'Reprovado'
print(turma1)

# 6. Mostre a quantidade de alunos aprovados e reprovados.
print(turma1['aprovado'].value_counts())
#print(df.loc[:, 'aprovado'].value_counts())
filtro_aprovado = turma1['aprovado'] == 'Aprovado'
print(f"Aprovado: {turma1.loc[filtro_aprovado, 'aprovado'].count()}")
print(f"Reprovado: {turma1.loc[~filtro_aprovado, 'aprovado'].count()}")

# Parte 7
turma1.to_csv('Exercicios_pandas/resultado_enem.csv', index=False)
