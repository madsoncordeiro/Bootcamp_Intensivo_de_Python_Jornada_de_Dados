# 1. Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

try:
    quantidade = int(input("Digite a quantidade de vendas: "))
    preco = float(input("Digite o preço de venda: "))

    if quantidade > 0 and preco > 0:
        print("Dados válidos. ")
    else:
        print("Dados inválidos. ")
except ValueError:
    print("Não é possível digitar algo diferente de números quando houver a solicitação da quantidade de vendas e do preço de venda. ")