from tkinter import N


print('====================')
print ('Calculo do salario!')
print('====================')

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:

salarioh = float(input('Digite seu salario Hora: R$'))
horast = float(input('Digite suas horas trabalhadas:'))
print('')
saltotal = salarioh * horast

print('+ Salário Bruto : R$',saltotal)
ir = saltotal*11/100
print('- IR (11%) : R$', ir)
inss = saltotal*8/100
print('- INSS (8%) : R$',inss)
sind = saltotal*5/100
print('- Sindicato ( 5%) : R$',sind )
desc = ir + inss + sind 
print('- Total de descontos R$', round (desc,2))
sallq = saltotal-desc
print('= Salário Liquido : R$',round (sallq,2))
print('')

print ('O desconto total do salario bruto (R$', saltotal,')')
print ('Foi de R$', desc,'O salario liquido ficou em,R$',sallq)
print('')
print('====================')