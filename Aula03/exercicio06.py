# 6. Dado um texto, contar quantas vezes cada palavra única aparece nele.

import string

texto = input("Digite um texto: ")

texto = texto.lower()
remover_pontuacao = str.maketrans("", "", string.punctuation)
texto = texto.translate(remover_pontuacao)
palavras = list(texto.split(" "))
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1