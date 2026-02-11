# 15. Dada uma string, contar a frequência de cada caractere usando um dicionário.

entrada: str = str(input("Digite o que quiser: "))
dicionario: dict = {}

for caractere in entrada:
    if caractere in dicionario:
        dicionario[caractere] += 1
    else:
        dicionario[caractere] = 1

print(dicionario)