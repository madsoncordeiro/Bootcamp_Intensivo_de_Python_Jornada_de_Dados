# 15. Processar itens de uma lista até encontrar um valor específico que indica a parada.
"""
[1, 2, 3, "parar", 4, 5]
"""

lista = [1, 2, 3, "parar", 4, 5]

while True:
    for elemento in lista:
        print(elemento)
        if elemento == "parar":
            exit()