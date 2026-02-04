# 25. Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

try:
    lista_numeros = input("Digite uma lista de números separados por vírgula (Por exemplo: 1,2,3): ")
    lista_numeros_string = lista_numeros.split(",")
    lista_numeros_inteiros = []
    
    for numero in lista_numeros_string:
        lista_numeros_inteiros.append(int(numero.strip()))
    print(f"Lista de números que você digitou: {lista_numeros_inteiros}")
except ValueError:
    print("Você não digitou os números no formato recomendado (1,2,3) ou não digitou número. ")