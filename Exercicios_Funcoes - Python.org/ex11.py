# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente,
# valide a data e retorne NULL caso a data seja inválida.


def mesExtenso(dia,mes,ano):
    if mes == 1:
        mes = 'janeiro'
    elif mes == 2:
        mes = 'fevereiro'
    elif mes == 3:
        mes = 'Março'
    elif mes == 4:
        mes = 'Abril'
    elif mes == 5:
        mes = 'Maio'
    elif mes == 6:
        mes = 'Junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'Agosto'
    elif mes == 9:
        mes = 'Setembro'
    elif mes == 10:
        mes = 'Outubro'
    elif mes == 11:
        mes = 'Novembro'
    elif mes == 11:
        mes = 'Dezembro'

    print(f'''A data por extenso é {dia} de {mes} de {ano} .''')
    

dia = int(input("Digite o Dia: \'DD\' "))
while dia not in range(1,32):
    print('Digite o mes valido, de 1 a 31: ') 
    dia = int(input("Digite o Dia: \'DD\' "))

mes = int(input("Digite o Més: \'M ou MM\' "))
while mes not in range(1,13):
    print('Digite o mes valido, de 1 a 12: ')
    mes = int(input("Digite o Més: \'MM\' "))

ano = input("Digite o Ano: \'AAAA\' ")

#while ano not in numeric(:
#    print('Digite o ano com 4 digitos:')
#    ano = int(input("Digite o Ano: \'AAAA\' "))
#print(f'''A data por extenso é {dia} de {mes} de {ano} .''')

mesExtenso(dia, mes, ano)