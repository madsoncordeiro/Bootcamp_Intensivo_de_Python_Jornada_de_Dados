# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def verificar_se_combinacao_de_numeros_sao_pares(lista_de_numeros: list[int], numero_alvo: int) -> list[tuple[int, int]]:
    
    lista_combinacao_de_pares: list = []
    
    for elemento in range(len(lista_de_numeros)):
        for element in range (elemento + 1, len(lista_de_numeros)):
            if lista_de_numeros[elemento] + lista_de_numeros[element] == numero_alvo and (lista_de_numeros[elemento] + lista_de_numeros[element]) % 2 == 0:
                lista_combinacao_de_pares.append((lista_de_numeros[elemento], lista_de_numeros[element]))
    return lista_combinacao_de_pares

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares: list = verificar_se_combinacao_de_numeros_sao_pares(lista_de_numeros, 12)

print(f"Pares: {pares}. ")