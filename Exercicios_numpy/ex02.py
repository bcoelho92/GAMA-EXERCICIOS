'''
2. Crie um array de duas dimensões, no formato 9x9,
com números de 0 a 80 ordenados de modo crescente e selecione:
  1. Os números ímpares
  2. Os números pares
  3. Os múltiplos de sete
  4. Os múltiplos de 10
  5. Os números 32,33,42,43

'''
import numpy as np
from numpy import arange

def pula():
    print()

# arange([start, ]stop, [step, ]dtype=None)
# Crie um array de duas dimensões,format 9x9,de 0 a 80 ordem crescente
array = arange(0,81).reshape(9,9)
pula()
print(array)
pula()
#  1. Os números ímpares
print(array[array %2 == 1])
pula()

# 2. Os números pares
print(array[array %2==0])
pula()

#  3. Os múltiplos de sete
print(array[array % 7==0])  
pula()

#  4. Os múltiplos de 10
print(array[ array % 10==0] ) 
pula()

#  5. Os números 32,33,42,43
print(array[3,[5,6,]], array[4,[6,7]])




