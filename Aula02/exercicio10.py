# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

try:
    raio = float(input("Digite o valor do raio do círculo: "))
    pi = 3.14159
    area = pi * (raio ** 2)

    print(f"O valor da área do círculo cujo raio é {raio:.2f} é igual a {area:.2f}. ")
except ValueError:
    print("Digite somente um número formado por algarismos. Não é possível utilizar o número por extenso. ")