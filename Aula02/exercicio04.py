# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    print(f"A divisão inteira de {numero1} por {numero2} é igual a {numero1 // numero2}. ")
except ValueError:
    print("Digite somente um número inteiro formado por algarismos. Não é possível utilizar o número por extenso ou número decimal. ")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero. Portanto, digite um número diferente de zero quando for solicitado para digitar o segundo número.")