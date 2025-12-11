# Peça a idade e informe se é maior de idade ou menor de idade.

# Solicita a idade do usuário
print("Bem-vindo ao verificador de idade!")
print("Por favor, informe sua idade.")
idade = int(input("Digite a sua idade: "))
# Verifica se a idade é maior ou igual a 18
# e imprime a mensagem correspondente
print("Você informou a idade:", idade)
print("Verificando se é maior de idade ou menor de idade...")
print("Aguarde um momento...")  
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")