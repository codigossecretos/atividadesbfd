# Peça a idade e, se for maior de idade, pergunte se tem habilitação (sim/não) e diga se pode dirigir.
idade = int(input("Digite sua idade: "))
if idade >= 18:
    habilitacao = input("Você tem habilitação? (sim/não): ")
    if habilitacao == "sim":
        print("Você pode dirigir.")
    elif habilitacao == "não":
        print("Você não pode dirigir.")
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
else:
    print("Você é menor de idade e não pode dirigir.")
print("Obrigado por participar!")
# Fim do código