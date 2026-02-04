# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if numero1 == numero2:
        print(f"Os números {numero1} e {numero2} que você digitou são iguais. ")
    else:
        print(f"Os números {numero1} e {numero2} que você digitou são diferentes. ")
except ValueError:
    print("Você digitou errado. Não pode ser digitado um número por extenso ou letras. Digite somente números. ")