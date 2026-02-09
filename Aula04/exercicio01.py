# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista: list = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for elemento in lista:
    print(f"{elemento}² = {elemento ** 2}")