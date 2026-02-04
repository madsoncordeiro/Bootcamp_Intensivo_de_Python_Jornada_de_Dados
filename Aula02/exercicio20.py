# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if numero1 != numero2:
        print(f"Os números {numero1} e {numero2} são diferentes. ")
    else:
        print(f"Os números {numero1} e {numero2} são iguais.")
except ValueError:
    print("Você digitou errado. Não pode ser digitado um número por extenso ou letras. Digite somente números. ")