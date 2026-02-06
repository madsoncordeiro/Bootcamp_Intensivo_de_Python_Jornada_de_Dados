# 7. Normalizar uma lista de números para que fiquem na escala de 0 a 1.

try:
    numeros_string = input("Digite uma lista de números separados por vírgula (Exemplo: 10,58,94):")
    lista_numeros = numeros_string.split(",")
    minimo = int(min(lista_numeros))
    maximo = int(max(lista_numeros))
    normalizados = []

    for numero in lista_numeros:
        normalizado = (float(numero) - minimo) / (maximo - minimo)
        normalizados.append(normalizado)

    print(normalizados)
except TypeError as erro:
    print("Você não digitou a lista de números conforme foi orientado. ")