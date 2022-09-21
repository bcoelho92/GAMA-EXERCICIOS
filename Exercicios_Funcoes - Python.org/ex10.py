import random
# random.randint(2,13)

# Jogo de Craps. Faça um programa de implemente um jogo de Craps.
# * O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# * Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
# * Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# * Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.


opcao = ''
rodada = 1
ponto = 0 
dado = random.randint(2,12+1) 

def jgcrap():
    print ("digite  \"sair\" para sair (sem aspas)\naperte <enter> para rolar os dados:\n ")
    opcao = str(input("Esperando acao: "))
    while opcao != 'sair':
        rodada =+ 1
        print(f"Jogada {rodada}")
        #opcao = str(input("Esperando acao: "))
        if opcao == "sair":
            print ("Saindo do jogo... Tchau")
        else:
            print(f"\n{dado}")

        if rodada ==1:
            if dado in (7,11):
                print ('Você tirou um natural e ganhou, PARABENS! \n')
                exit()
            elif dado in (2,3,12):
                print ('Você tirou um craps e perdeu, melhor sorte da proxima vez! \n')
                exit()
        else:
            ponto = dado
            if dado == ponto:
                print ('Voce conseguiu repetir seu ponto e ganhou, Parabens!')
                print(dado)
                print(ponto)
                exit()
            elif dado == 7:
                print("Você perdeu!")
                exit()
jgcrap()



