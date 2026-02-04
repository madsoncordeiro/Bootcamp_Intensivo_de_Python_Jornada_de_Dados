# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

try:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = float((celsius * 1.8) + 32)

    print(f"A temperatura de {round(celsius, 2)}°C corresponde a {round(fahrenheit, 2)}°F. ")
except ValueError:
    print("Digite somente um número formado por algarismos. Não é possível utilizar o número por extenso. ")