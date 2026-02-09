# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã":0.45, "banana":0.30, "cereja":0.65}, calcule o preço total da lista de compras.

lista:list = list["maçã", "banana", "cereja"]
dicionario: dict = {"maçã":0.45, "banana":0.30, "cereja":0.65}

for preco in dicionario:
    preco_total: float = float(sum(dicionario.values()))

print(f"Preço total: R${preco_total:.2f}.")