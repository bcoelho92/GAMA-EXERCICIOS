# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu principal e Sub Menus - Bruno
# 1 - Cadastro - Julia (Bruno backup) 
# 2 - Vendas - Fernando (Bruno backup) 
# 3 - Relatorio - relatorio sera desenvolvido de acordo com as entregas.

####################################################################################

# Boas vindas / 0 - Men

from time import sleep 


def menuV():
    menuV()

def menuR():
    menuR()

#####################################################################
print()
nomeCliente = str(input('Digite sue nome: '))

print('''
***********************************************************
 Bem vindo(a) {} ao sistema de vendas da Organico’s! 
                                                     
 Digute o numero da opção que você deseja:           
                                                     
 [1] - Cadastro                                 
 [2] - Vendas                                   
 [3] - Relatório                                
 [4] - Sair                                     
                                                     
***********************************************************
'''.format(nomeCliente))

menu = int(input('Digite a opção: '))
print()

def main():
    while True:
        #menu = int(input('Digite a opção: '))
        #print()
        if menu == 1:
            print ('{}, você esta no menu CADASTRO:'.format(nomeCliente))
            print('''
***********************************************************
- Digute o numero da opção que você deseja:           
                                                    
    [1] - Cadastramento de produtos                                 
    [2] - Listar produtos cadastrados 
    [3] - Deleção de produtos                                  
    [4] - Retornar ao menu principal                                
    [5] - Encerrar programa                                    
                                                    
***********************************************************
                    '''.format(nomeCliente))
            def menuC():  
                while True:
                    menu2 = int(input('Digite a opção: '))
                    if menu2 == 1:
                        print('Vamos cadastrar')
                    elif menu2 ==2:
                        print('Lista de produtos')
                    elif menu2 == 3:
                        print('Deletar produtos')
                    elif menu2 == 4:
                        print('Retrnar ao menu principal')
                        main()
                    elif menu2 == 5:
                        print('Fim do programa')
                        break
                    else:
                        print('Digite a opção valida: ')
                        
                menuC()


        elif menu ==2:
            print('Lista de produtos')
            
        elif menu == 3:
            print('Deletar produtos')
            
        elif menu == 4:
            print('Fim do programa')
            break
        else:
            print('Digite a opção valida: ')
            main()
            sleep(2)
main()