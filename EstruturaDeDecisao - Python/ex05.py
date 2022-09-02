# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:

print ('='*20)
print ('Média + aprovado(a) ou reprovado(a)!')
print ('='*20)

nota = float(input('Digite a 1º nota: ')) 
nota1 = float(input('Digite a 2ª nota: '))

media = (nota+nota1)/2

print ('')

if media >= 7: print ('Você foi aprovado(a) :) sua média foi de ', media)
elif  media == 10: print ('Você foi aprovado(a) com Distinção, sua média foi 10 Parabens!')
elif media <= 7: print ('Você foi reprovado(a) :( sua médoa foi de ', media)

print ('='*20)