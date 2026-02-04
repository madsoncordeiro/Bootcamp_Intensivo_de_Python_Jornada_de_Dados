# 21. Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = float((celsius * 1.8) + 32)

    print(f"A temperatura de {round(celsius, 2)}°C corresponde a {round(fahrenheit, 2)}°F. ")
except ValueError:
    print("Digite somente um número formado por algarismos. Não é possível utilizar o número por extenso. ")