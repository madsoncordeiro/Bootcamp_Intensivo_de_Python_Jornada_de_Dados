# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

try:
    numero = int(input("Digite um número: "))

    print(f"O quadrado de {numero} é igual a {numero * numero}. ")
except ValueError:
    print("Digite somente um número inteiro formado por algarismos. Não é possível utilizar o número por extenso ou número decimal. ")