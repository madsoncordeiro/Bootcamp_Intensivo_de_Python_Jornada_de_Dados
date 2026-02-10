# 9. Dado um conjunto de números, calcular a média.

numeros:list = [10, 20, 30, 40, 50]
soma:int = int(sum(numeros))
quantidade_numeros:int = int(len(numeros))
media:float = soma / quantidade_numeros

print(f"Média = {media}. ")