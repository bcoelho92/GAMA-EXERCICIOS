# (8) - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

print ("Contando! ")

def quatDig(valor):
    resut = len(valor)
    print(f" a quantidade de caracteres é {resut}")

valor = str(input("Digite um valor: "))

quatDig(valor)

print('\nNa vertical fica assim:\n')
for letra in valor: # PRINT LETRAS NA VERTICAL, VAI PEGAR CADA LETRA E PRINT EM 1 LINHA.
    print(letra)

print()