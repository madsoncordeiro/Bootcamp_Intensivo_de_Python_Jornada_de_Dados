# 12. Dados dois dicionários, fundi-los em um único dicionário.

dicionario1: dict = {"a":1, "b":2}
dicionario2: dict = {"c":3, "d":4}

dicionario_unico: dict = {}

for valor in dicionario1:
    dicionario_unico.update(dicionario1)
for valor in dicionario2:
    dicionario_unico.update(dicionario2)

print(dicionario_unico)