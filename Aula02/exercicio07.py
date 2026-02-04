# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    soma = numero1 + numero2
    media = soma / 2

    print(f"A média entre os números {numero1} e {numero2} é igual a {round(media, 2)}. ")
except ValueError:
    print("Digite somente um número formado por algarismos. Não é possível utilizar o número por extenso. ")