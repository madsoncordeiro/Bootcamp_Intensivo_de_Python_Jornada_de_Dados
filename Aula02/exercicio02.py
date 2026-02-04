# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

try:
    numero = int(input("Digite um número: "))

    print(f"O resto da divisão de {numero} por 5 é igual a {numero % 5}. ")
except ValueError:
    print("Digite somente um número inteiro formado por algarismos. Não é possível utilizar o número por extenso ou número decimal. ")