# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte 
# critério, baseado no salário atual:
print('')
salario = float(input('Digite o seu salario: R$ '))

print('')

# salários até R$ 280,00 (incluindo) : aumento de 20%
if salario <= 280 : 
    print ('- O seu salario é R$ ',salario)  
    print ('- O percentual de aumento é de 20%')
    print ('- O valor do aumento é de R$', salario*0.20) 
    print ('- O novo salário, após o aumento é de R$ ', salario + (salario*0.20))

# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif salario >= 280 and salario < 700 : 
    print ("- O seu salario é R$",salario)  
    print ('- O percentual de aumento é de 15%')
    print ('- O valor do aumento é de R$', salario*0.15) 
    print ('- O novo salário, após o aumento é de R$ ', salario + (salario*0.15))

# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif salario > 700 and salario <= 1500 : 
    print ("- O seu salario é R$",salario)  
    print ('- O percentual de aumento é de 10%')
    print ('- O valor do aumento é de R$', salario*0.10) 
    print ('- O novo salário, após o aumento é de R$ ', salario + (salario*0.10))

# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 
elif salario > 1500 : 
    print ("- O seu salario é R$",salario)  
    print ('- O percentual de aumento é de 5%')
    print ('- O valor do aumento é de R$', salario*0.05) 
    print ('- O novo salário, após o aumento é de R$ ', salario + (salario*0.05))

print ('')
print ('Fim do programa.')
print ('')



