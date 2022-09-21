# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.

def arg (n1,n2): 
    if n1 and n2 > 0:
        print("P")
    else: print ("N")

print ("A maior que B ?")
arg(int(input("Digite A: ")),int(input("Digite B: ")))