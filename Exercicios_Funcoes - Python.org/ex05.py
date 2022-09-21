# Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem 
# custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):

    custoFinal = custo*(1+taxaImposto/100)
    print (f'''
    ********************
    Seu produto custa: R$ {custo}
    O valor total do seu produto é R$  R$ {custoFinal}
    ********************
    ''')
    
somaImposto(float(input("\nDigite a porcentagem: % " )) ,float(input("Digiteo o valor: R$ ")))
