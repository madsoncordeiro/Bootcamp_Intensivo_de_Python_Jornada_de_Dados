# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista:list = list(["Python", "Java", "C++", "JavaScript"])
print(f"Lista inicial: {lista}. ")

lista.remove("C++")
lista.append("Ruby")

print(f"Lista final após remover o 'C++' e adicionar o 'Ruby': {lista}. ")