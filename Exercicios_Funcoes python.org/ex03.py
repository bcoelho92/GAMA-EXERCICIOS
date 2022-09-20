# Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.



def soma(n1='',n2='',n3=''):
    r = n1+n2+n3
    print (f'''
    A soma de {n1} {n2} e {n3} é igaul a {r}
    ''')
    return r

n1 = int(input('digite 1 valores: '))
n2 = int(input("Segundo valor: "))
n3 = int(input("terceiro valor: "))

resutado = soma(n1, n2, n3)
print("este é o resutado fora do função: ", resutado)

