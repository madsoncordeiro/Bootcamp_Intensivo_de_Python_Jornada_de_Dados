# 14. Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario: dict = {"a":1, "b":2, "c":3}
chaves: list = []
valores: list = []

for chave, valor in dicionario.items():
    chaves.append(chave)
    valores.append(valor)

print(f"""
Chaves: {chaves}.
Valores: {valores}.
      """)