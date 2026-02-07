"""
DESAFIO - Cálculo de Bônus com Entrada do Usuário

Escreva um programa, em Python, que solicita ao usuário para que digite seu nome, valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome, além de informar o valor do salário em comparação com o bônus recebido.
"""

nome_usuario = input("Digite o seu nome: ")
salario_usuario = float(input("Digite o seu salário: "))
bonus_usuario = float(input("Digite o valor do bônus que você recebeu: "))

kpi_bonus = 1000 + (salario_usuario * bonus_usuario)

print(f"Olá, {nome_usuario}. O seu valor bônus foi de R${kpi_bonus}.")