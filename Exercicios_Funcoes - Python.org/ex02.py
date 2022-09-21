p = int(input('N: '))
def linha (parada):
    numero=1
    texto = str(numero)
    print (texto)

    while numero < parada:
        numero = numero + 1
        texto = texto + ' ' + str(numero)
        print(texto) 
        
linha(p)