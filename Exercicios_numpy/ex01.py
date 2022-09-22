'''
1. Utilizando a biblioteca numpy siga as instruções abaixo:
    1. Crie um array 6x6 preenchido com zero
    2. Preencha o centro desse array com um array 4x4 preenchido com uns
    3. Preencha o centro desse array com um array 2x2 preenchido com dois
    4. Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2.
    5. Subtraia o primeiro array pelo segundo
'''
import numpy as np

# import da biblioteca definir apelido usar "as"
'''
from numpy import arange 
from numpy import reshape
'''
# incurtar o camando de np.arange(21,dtype=int) para arange(21,dtype=int)

# 1. Crie um array 6x6 preenchido com zero.

# lista = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
muda = np.zeros([6,6])
#print(muda)

# 2. Preencha o centro desse array com um array 4x4 preenchido com uns.
muda1 = np.zeros([6,6])
muda1 [1:5, 1:5] = 1 # seleciona o quadrante e substitui o valor por 1.
# print(muda1)

#  3. Preencha o centro desse array com um array 2x2 preenchido com dois
muda1 [2:4, 2:4] = 2
# print(muda1)

# 4. Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2.
muda2 = np.random.randint(low=0, high=3, size=[1,6,6])
/
print(muda1)
print()
print(muda2)
print()
/
# 5. Subtraia o primeiro array pelo segundo
muda3 = muda1-muda2
print(muda3) 


