# teste menu 
import os

print()
print('Vamos começar!\n')
nomeCliente = str(input('Olá, Digite seu nome: '))

print('''
***********************************************************
 Bem vindo(a) {} ao sistema de vendas da Organico’s! 
                                                     
 Digute o numero da opção que você deseja:           
                                                     
 [1] - Menu Cadastro                                 
 [2] - Menu Vendas                                   
 [3] - Menu Relatório                                
 [4] - Sair                                     
                                                     
***********************************************************
'''.format(nomeCliente))

# variaveis 

menu = int(input('Digite a opção: '))

#while menu >=5 or menu <=0:
#    menu = int(input('Digite a opção valida: '))
#    os.system('clear')
       
if menu == 1:
    print ('Menu cadastro')
    print('''
***********************************************************
 {}, digute o numero da opção que você deseja:           
                                                     
    [1] - Cadastramento de produtos                                 
    [2] - Listar produtos cadastrados 
    [3] - Deleção de produtos                                  
    [4] - Retornar ao menu principal                                
    [5] - Encerrar programa                                    
                                                     
***********************************************************'''.format(nomeCliente))
    menu2 = int(input('Digite a opção: '))
    def main1():
        #while True:
            if menu2 == 1:
                print('Vamos cadastrar')
            elif menu2 ==2:
                print('Lista de produtos')
            elif menu2 == 3:
                print('Deletar produtos')
            elif menu2 == 4:
                print('Retrnar ao menu principal')
            elif menu2 == 5:
                print('Fim do programa')
                #break
            else:
                print('Digite a opção valida: ')
                main1()


elif menu == 2:
        print('Menu vendas')
        n1 = float(input('digite primeiro numero: '))
        n2 = float(input('digite segundo numero: '))
        r = n1-n2
        print ('A Subtração de {} e {} é igaul {}'.format(n1,n2,r))


elif menu == 3:
        print('Menu relatorio')
        n1 = float(input('digite primeiro numero: '))
        n2 = float(input('digite segundo numero: '))
        r = n1*n2
        print ('A multi de {} e {} é igaul {}'.format(n1,n2,r))

elif menu == 4:
        print('Sair, grato pelo seu acesso!')

#print('')
#print('fim do programa!')