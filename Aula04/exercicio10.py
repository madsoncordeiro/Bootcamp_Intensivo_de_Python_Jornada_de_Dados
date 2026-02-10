# 10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares:list = []
impares:list = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f"""
Pares: {pares}.
Ímpares: {impares}.""")