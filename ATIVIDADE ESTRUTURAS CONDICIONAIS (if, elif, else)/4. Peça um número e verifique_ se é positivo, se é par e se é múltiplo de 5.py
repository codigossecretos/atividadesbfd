# Peça um número e verifique: se é positivo, se é par e se é múltiplo de 5.

numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    
    if numero % 5 == 0:
        print("O número é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 5.")
else:
    print("O número não é positivo.")
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    
    if numero % 5 == 0:
        print("O número é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 5.")