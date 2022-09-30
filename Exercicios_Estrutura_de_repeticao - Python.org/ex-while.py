import sys
import numpy as np
import pandas as pd

numero=[]
i="n"

while i == "n":
    numero.append(int(input("Acidicone quantos numero quiser: ")))
    i = str(input("Deseja Sair ? s/n "))

numeros = pd.Series(numero, name='numeros')
print(f'''Esses sao os numeros cadastrados:
{numeros}''') 
print()
i="n"

while i == "n":
    numero.remove(int(input(f"Digite o numero {i} de 5 que deseja remover: ")))
    i = str(input("Deseja Sair ? s/n "))

numeros = pd.Series(numero, name='numeros')
print(f'''esses sao os numeros que restaram:
{numeros}''')
print()

print("Fim")
