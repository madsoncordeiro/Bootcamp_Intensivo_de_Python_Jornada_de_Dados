# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
media = soma / 2

print(f"A média entre os números {numero1} e {numero2} é igual a {round(media, 2)}. ")