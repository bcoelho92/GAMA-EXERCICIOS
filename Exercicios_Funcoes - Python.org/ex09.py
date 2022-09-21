# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721.

print ("\n Retorne o reverso! \n")

def reverter(n):
    n = "".join(reversed(n)) 
    print(f'\nRevertido fica assimn: {n}\n')
    return n 
    
n = str(input("Digite um numero: "))

reverter(n)
