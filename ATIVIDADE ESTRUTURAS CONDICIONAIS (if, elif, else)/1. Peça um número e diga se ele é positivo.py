# Peça um número e diga se ele é positivo
# Solicita se o número para verificação
referencia = 0
verificando = int(input("Digite o número para ser verificado:"))

# Verificando número
if verificando > referencia:
    print ("Número Positivo")

elif verificando == referencia:
    print ("É zero")

else:
    print ("Número Negativo")