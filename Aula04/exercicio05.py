# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã":0.45, "banana":0.30, "cereja":0.65}, calcule o preço total da lista de compras.

lista:list = ["maçã", "banana", "cereja"]
dicionario: dict = {"maçã":0.45, "banana":0.30, "cereja":0.65}
preco_total: float = float(0.0)

for item in lista:
    preco_total += dicionario[item]

print(f"Preço total: R${preco_total:.2f}.")