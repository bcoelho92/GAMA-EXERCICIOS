'''

def pula():
    print()

pula()
# Adicionar item na lista 

teste = []
teste.append('c')
print(teste)
pula()

# estender ou juntar listas 

teste2 = ['d','b','a']
teste.extend(teste2) # Este exemplo deixa teste2 intocado.
print(teste)
pula()

# Classifica os elementos da lista em ordem ascendente / crecente:
teste.sort()
print(teste)
pula()

# Adionando um indice 

teste.index('a')
print(teste)
pula()
'''
'''
import numpy as np

array = np.array([1,2,3,4,5,5,6,7,8,8,9,9])

result = np.clip(array, 0, 9)
print(result)


# numpy.arange([start, ]stop, [step, ]dtype=None)
teste = np.arange(36)
teste = teste.reshape([6,6])


print(teste)

'''