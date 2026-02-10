# 11. Dada uma lista de dicionários representando produtos, atualizar o preço do produto com id 2 para 90.

produtos: list = [
    {"id":1, "nome":"Teclado", "preco":100},
    {"id":2, "nome":"Mouse", "preco":80},
    {"id":3, "nome":"Monitor", "preco":300}
]

for valor in produtos:
    if valor["id"] == 2:
        valor["preco"] = 90

print(produtos)