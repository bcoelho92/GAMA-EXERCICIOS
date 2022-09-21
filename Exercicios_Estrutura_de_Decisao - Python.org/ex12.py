# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda,
#  que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

print('')
print ('** Folha de pagamento ** ')
print('')

horas = float(input('Digite o numero de horas trabalhadas:'))
ghoras = float(input('Digite o ganho por horas:'))

salbru = horas*ghoras

sindsal = (3 /100.0) *salbru

cinco = (5 / 100.0) * salbru
dez = (10 / 100.0) * salbru
vinte = (20 / 100.0) * salbru
onze = (11 / 100.0) * salbru

if salbru <= 900:
       print ('Seu salário bruo é de:', salbru)
       print ('(-) IR  = (isento)')
       print ('(-) INSS ( 10%):','R$',dez)
       print ('FGTS (11%): ','R$',onze)
       print ('Total de descontos:','R$', dez + onze)
       print ('Salário Liquido :','R$ ', salbru -(dez+onze))

elif salbru > 900 and salbru <= 1500:
       print ('Seu salário bruo é de:', salbru)
       print ('(-) IR (5%) :','R$',cinco)
       print ('(-) INSS ( 10%):','R$',dez)
       print ('FGTS (11%): ','R$',onze)
       print ('Total de descontos:','R$',cinco + dez + onze)
       print ('Salário Liquido :','R$ ', salbru - (cinco+dez+onze))

elif salbru > 1500 and salbru <= 2500:
    print ('Seu salário bruo é de:', salbru)
    print ('(-) IR (10%) :','R$',dez)
    print ('(-) INSS ( 10(10%)%):','R$',dez)
    print ('FGTS (11%): ','R$',onze)
    print ('Total de descontos:','R$',dez + dez + onze)
    print ('Salário Liquido :','R$ ', salbru - (dez+dez+onze))

elif salbru > 1500 and salbru <= 2500:
    print ('Seu salário bruo é de:', salbru)
    print ('(-) IR (20%) :','R$',vinte)
    print ('(-) INSS ( 10%):','R$',dez)
    print ('FGTS (11%): ','R$',onze)
    print ('Total de descontos:','R$',vinte + dez + onze)
    print ('Salário Liquido :','R$ ', salbru - (vinte+dez+onze))


print('')
print('Fim do calculo!')
print ('')

