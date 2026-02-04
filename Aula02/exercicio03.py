# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    print(f"A multiplicação de {numero1} por {numero2} é igual a {numero1 * numero2}. ")
except ValueError:
    print("Digite somente um número inteiro formado por algarismos. Não é possível utilizar o número por extenso ou número decimal. ")