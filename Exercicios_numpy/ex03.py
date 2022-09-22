'''
3. Crie um array com três dimensões, 
onde a primeira dimensão são os dias da semana (seg a dom),
a segunda dimensão são as semanas do mês (considere apenas 4 para todos os meses),
e a terceira são os meses do ano (Jan a dezembro).

  1. Marque os finais de semana com a letra W
  2. Marque o começo do mês com a letra S
  3. Marque o final do mês com a letra E
  4. Marque os demais dias com a letra D
  5. Marque os feriados nacionais com a letra F
    - 01/01 - Ano novo
    - 15/04 - Paixão de Cristo
    - 21/04 - Tiradentes
    - 01/05 - Dia do Trabalho
    - 07/09 - Independência do Brasil
    - 12/10 - Nossa Senhora Aparecida
    - 02/11 - Finados
    - 15/11 - Proclamação da República
    - 25/12 - Natal
PS: o enunciado está com a dimensões invertidas. ;D
'''

import numpy as np

array = np.arange(1,29,dtype=object).reshape(1,4,7)
calendario = np.repeat(array,12, axis=0)

# 1. Marque os finais de semana com a letra W
calendario[:,:,[0,-1]] = 'w'

# 2. Marque o começo do mês com a letra S
calendario[:,0,0] = 's'
# 3. Marque o final do mês com a letra E
calendario[:,-1,-1] = 'e'
# 4. Marque os demais dias com a letra D
calendario[:, :, 1:-1] = 'd'
# np.isin(calendario, ['w','s','e'])

#   5. Marque os feriados nacionais com a letra F

# calendario[mes. semana, dia ]

'''- 01/01 - Ano novo
  - 15/04 - Paixão de Cristo
  - 21/04 - Tiradentes
  - 01/05 - Dia do Trabalho
  - 07/09 - Independência do Brasil
  - 12/10 - Nossa Senhora Aparecida
  - 02/11 - Finados
  - 15/11 - Proclamação da República
  - 25/12 - Natal'''

print(calendario)
