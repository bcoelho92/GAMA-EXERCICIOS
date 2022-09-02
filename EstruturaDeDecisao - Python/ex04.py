# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print ('='*20)
print ('Vogal ou consolante')
print ('='*20)

letra = str(input("Digite uma letra do alfabeto (letra minuscula): "))
print ('')

if letra == "a":
    print ('A letra', letra,'é Vogal!')
elif letra =="e":
    print ('A letra', letra,'é Vogal!')
elif letra =="i":
    print ('A letra', letra,'é Vogal!')
elif letra == "o":
    print ('A letra', letra,'é Vogal!')
elif letra == "u":
    print ('A letra', letra,'é Vogal!')


# if not letra.isalpha():
#    print ('Não é um caracer valido')
# elif letra in "aeiou":
#   print ("Vogal") 
# else: print ('Consoante')



else:
    print ('A letra',letra,'é Consoante!')

print ('='*20)