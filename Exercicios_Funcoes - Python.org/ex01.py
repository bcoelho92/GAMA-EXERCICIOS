# print a quantidade de linhas que o usuario desejar 

def dig (n):
    for linha in range(n+1):
        print((str(linha)+'')*linha)

dig(int(input("Digite o numero: ")))