# 13. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que zero.

estoque:dict = {"Teclado":10, "Mouse":0, "Monitor":3, "CPU":0}
estoque_com_produto: dict = {}

for chave, valor in estoque.items():
        if valor > 0:
            estoque_com_produto[chave] = valor

print(estoque_com_produto)