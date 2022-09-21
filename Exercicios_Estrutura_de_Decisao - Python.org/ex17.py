#Faça um Programa que peça um número correspondente a um determinado
#  ano e em seguida informe se este ano é ou não bissexto.

'''
ano
4 > bissexto
100 nao é bissexto
400 é bissexto
'''
print('='*20)
print('Ano bissexto ou não?')
print('='*20)


ano = int(input('Ano: '))
print ('')

if (ano%4==0 and ano%100!=0) or (ano%400==0): 
# Resto do ano tem que ser dividido e o resto igual a zero Ex: "ano%4==0"
# true amd false or true 
# false or true 
# true
    print('Bissexto')
else:
    print('Não é bissexto')
    
print('')
print('='*20)
print('Fim do programa!')
print('='*20)