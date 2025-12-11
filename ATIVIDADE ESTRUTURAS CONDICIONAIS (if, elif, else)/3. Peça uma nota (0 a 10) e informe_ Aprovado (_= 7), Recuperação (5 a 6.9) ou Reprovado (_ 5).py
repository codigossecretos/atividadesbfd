# Peça uma nota (0 a 10) e informe: Aprovado (>= 7), Recuperação (5 a 6.9) ou Reprovado (< 5).
nota = float(input("Digite a nota (0 a 10): "))
# A nota deve estar entre 0 e 10, caso contrário, uma mensagem de erro será exibida.
# A nota é verificada e a mensagem correspondente é exibida com base na condição atendida.
# Se a nota for maior ou igual a 7, o aluno é aprovado.
if nota >= 7:
    print("Aprovado")
# Se a nota estiver entre 5 e 6.9, o aluno está em recuperação.
elif 5 <= nota < 7:
    print("Recuperação")
# Se a nota for menor que 5, o aluno é reprovado.
elif 0 <= nota < 5:
    print("Reprovado")
# Se a nota for inválida (fora do intervalo de 0 a 10), uma mensagem de erro é exibida.
else:
    print("Nota inválida. Digite uma nota entre 0 e 10.")






