# 10. Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""
[
    {"categoria":"eletrônicos", "valor":"1200"},
    {"categoria":"livros", "valor:200"},
    {"categoria":"eletrônicos", "valor":"800"}
]
"""

registros_vendas = [
    {"categoria":"eletrônicos", "valor":"1200"},
    {"categoria":"livros", "valor":"200"},
    {"categoria":"eletrônicos", "valor":"800"}
]

lista_categorias = {}

for registro in registros_vendas:
    categoria = registro["categoria"]
    valor = float(registro["valor"])
    
    if categoria in lista_categorias:
        lista_categorias[categoria] += valor
    else:
        lista_categorias[categoria] = valor

print(lista_categorias)    