# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

try:
    base = float(input("Digite um número: "))
    expoente = float(input("Digite o expoente: "))
    potencia = base ** expoente

    print(f"O número {base} elevado a {expoente} é igual a {round(potencia, 2)}. ")
except ValueError:
    print("Digite somente um número formado por algarismos. Não é possível utilizar o número por extenso. ")