# Peça a cor do semáforo (verde, amarelo, vermelho) e exiba a ação correspondente.
cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ")
if cor == "verde":
    print("Pode seguir.")
elif cor == "amarelo":
    print("Atenção, reduza a velocidade.")
elif cor == "vermelho":
    print("Pare.")
else:
    print("Cor inválida. Por favor, digite verde, amarelo ou vermelho.")
# Fim do código
