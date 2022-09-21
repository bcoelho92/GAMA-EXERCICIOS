print()
nomeCliente = str(input('Digite sue nome: '))

def main():
    while True:
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
        
        if menu == 1:
            print ('Cadastro')
        elif menu == 2:
            print ('Vendas')
        elif menu == 3:
            print ('Relatorio ')
        elif menu == 4:
            print('fim do programa')
            break
        else: 
            print('Digite a opção valida: ')
            main()
main() 
