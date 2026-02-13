# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.

def dicionario_para_lista_de_chaves_ordenadas(dicionario: dict) -> list:
    return sorted(dicionario.keys())

dicionario_usuario: dict = {"c":5, "a":2, "b":4}
lista_de_chaves_ordenadas : list = dicionario_para_lista_de_chaves_ordenadas(dicionario_usuario)

print(f"Lista de chaves ordenadas: {lista_de_chaves_ordenadas}. ")