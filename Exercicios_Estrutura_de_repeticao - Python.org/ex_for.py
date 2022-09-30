import sys
import numpy as np
import pandas as pd

# validar numero mairo de um conjunto de 10 digitados

numero=[]
cont=10
i=0
for i in range(1,11):
    numero.append(int(input(f"Difite o numero {i} de {cont}: ")))
maior = max(numero)
menor = min(numero)   
print(f"o maior numero é {maior} e o menor numeor é {menor}.")
print("Fim")



