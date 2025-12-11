# Atividade Extra Python Input

#Lógica
#Biblioteca para inferir o ano corrente
from datetime import date

#Encontra o ano corrente
ano_atual = date.today().year

#Solicita o ano de nascimento
ano_de_nascimento = int( input("Para saber sua idade, Digite seu ano de nascimento:"))

#Calcula a idade
idade = ano_atual - ano_de_nascimento 

#Mostra o resultado
print(idade)
