import numpy as np

array = np.arange(36)
array = array.reshape([6,6])
#seleção
array[2]
array[2,:]
array[:, 2]
array[2:5, 1:4]
array[2:-1, 1:-2]
array[:,[1,3,5]]
array[:,1::2]
array[::2,:]
linha = 1
coluna = 2
array[linha:,coluna:]
coluna = [1,2,3,5]
linha = [0,2,4,5]
array[:, [1,2,3,5]]
array[linha, :]
# coordenadas (batalha naval)
array[linha, coluna]
# diagonais
array.diagonal()
array.diagonal(1)
array.diagonal(-1)
array[:,::-1].diagonal()
# mascaras
array[array %2 == 0]
filtro_pares = array %2 == 0
array[filtro_pares]
filtro_impar = array %2 == 1
teste = array[filtro_impar].reshape()

print(teste)