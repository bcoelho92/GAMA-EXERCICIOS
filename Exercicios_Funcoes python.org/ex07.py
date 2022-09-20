# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, 
# que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.



def valorPagamento(valPres, diaAtras):
    if diaAtras == 0:
        print(f'\nO valor a ser pago sem dias de atrso é R$ {valPres} .')
    elif diaAtras > 0:
        valJur = valPres*(1+3/100) 
        valJur = valJur*(1+diaAtras/100)
        print(f'''
        
        Você esta com {diaAtras} dias de atraso.
        Em caso de atraso é cobrado 3% de multa, mais 0,1% de juros por dia de atraso.

        O valor a ser pago com juros e correção é R$ {valJur} .
        
        ''')
valorPagamento(float(input("\nValor da prestação: ")), int(input("Dias em atraso: ")))

