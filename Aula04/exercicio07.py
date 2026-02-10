# 7. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades:list = [22, 15, 30, 17, 18]

lista_filtrada:list = []

for idade in idades:
    if idade >= 18:
        lista_filtrada.append(idade)

print(f"Idades maiores ou iguais a 18: {lista_filtrada}. ")