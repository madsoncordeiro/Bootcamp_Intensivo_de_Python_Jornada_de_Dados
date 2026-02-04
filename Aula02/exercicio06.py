# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

try:
    numero1 = float(input("Digite o primeiro número decimal: "))
    numero2 = float(input("Digite o segundo número decimal: "))

    print(f"A soma entre {numero1} e {numero2} é igual a {round(numero1 + numero2, 2)}. ")
except ValueError:
    print("Digite somente um número inteiro formado por algarismos. Não é possível utilizar o número por extenso. ")