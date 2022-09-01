# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa 
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável 
# excesso a quantidade de quilos além do limite e na variável multa o valor da multa
# que João dever# 

print ('='*22)
print (' João Papo-de-Pescador')
print ('='*22)

peso = float(input('Peso> ')) 
excesso = 0
multa = 0 

if  peso > 50 : # if entao / if ":"
    excesso = (peso-50)
    multa = excesso * 4.00

# print ('Peso', peso,'Kg')
print ('Excesso', excesso, 'Kg')
print ('Multa de R$', multa, )











