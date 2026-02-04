# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    print(f"{numero1} + {numero2} = {numero1 + numero2}. ")
except ValueError:
    print(f"Insira somente o(s) algarismo(s) dos números. Não pode inserir o número por extenso ou número decimal. ")