"""
DESAFIO da Aula01
Escreva um programa, em Python, que solicita ao usuário para que digite seu nome, valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome, além de informar o valor do salário em comparação com o bônus recebido.

DESAFIO da Aula02
Refatorar o projeto da aula anterior evitando bugs.

DESAFIO da Aula03
Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas.
"""

while True:
    try:
        nome_usuario = input("Digite o seu nome: ")
        if nome_usuario.isdigit():
            raise ValueError("Você digitou um número no lugar do nome. Isso não é permitido. ")
        elif len(nome_usuario) == 0:
            raise ValueError("Você não digitou o seu nome e deixou o campo vazio. Isso não é permitido. ")
        elif nome_usuario.isspace():
            raise ValueError("Você digitou apenas espaço em branco no lugar do seu nome. Isso não é permitido. ")
        
        salario_usuario = float(input("Digite o seu salário: "))
        bonus_usuario = float(input("Digite o valor do bônus que você recebeu (digite somente o número): "))
        
        if salario_usuario >= 0 and bonus_usuario >= 0:
            kpi_bonus = 1000 + (salario_usuario * bonus_usuario)
            print(f"Olá, {nome_usuario}. O seu valor bônus foi de R${kpi_bonus}.")
            exit()
        else:
            print("Você digitou um número negativo para o salário, para o bônus ou para ambos. ")

    except ValueError as erro:
        print(erro)