# 22. Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: utilize a função isinstance() para verificar o tipo de entrada.

try:
    string = input("Digite uma palavra ou frase qualquer: ")
    if isinstance(string, str):
        print("Você digitou realmente uma palavra ou frase qualquer. ")
        print("")
        if string == string[::-1]:
            print("O que você digitou é um palíndromo. ")
        else:
            print("O que você digitou não é um palíndromo. ")
except AttributeError:
        print("Houve erro de lógica no código. ")
    