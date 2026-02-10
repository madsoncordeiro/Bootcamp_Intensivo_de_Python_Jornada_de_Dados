# 8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

from operator import itemgetter

pessoas:list = [
    {"nome":"Alice", "idade":30},
    {"nome":"Bob", "idade":25},
    {"nome":"Carol", "idade":20}
]

lista_ordenada:list = sorted(pessoas, key = itemgetter("nome"))

print(lista_ordenada)