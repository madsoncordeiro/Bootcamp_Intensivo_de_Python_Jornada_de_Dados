from typing import Dict, Any
import json

produto_01: Dict[str, Any[int, str, bool]]

idade: int = 30
altura: float = 1.75
nome: str = "Alice"
is_estudante: bool = True

produto1: str = "sapato"
produto2: str = "camiseta"
produto3: str = "videogame"

produtos: list = []

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)

print(produtos)

produtos.pop()
produtos.remove(produto2)

print(produtos)

numeros = []
numeros.extend(range(1,6))
print(numeros)

lista: list = ["Sapato", 39, 10.38, True]

produto_01: dict = {
    "nome":"Sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True
}

produto_02: dict = {
    "nome":"Televisão",
    "quantidade":10,
    "preco":70.38,
    "disponibilidade":False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)