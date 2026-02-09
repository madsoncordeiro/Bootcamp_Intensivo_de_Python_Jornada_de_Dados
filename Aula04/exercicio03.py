# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

try:
    titulo: str = str(input("Qual o título do livro? "))
    autor: str = str(input("Qual o nome do autor? "))
    if titulo.isdigit() or autor.isdigit():
        print("Você digitou um número quando solicitado o nome do título ou do autor. ")
        exit()
    ano_publicacao: str = str(input("Qual o ano de publicação? "))
    if not ano_publicacao.isdigit():
        print("Você não digitou um número para informar qual o ano de publicação do livro. ")
        exit()

    livro: dict = dict({"titulo":titulo, "autor":autor,"ano_publicacao":ano_publicacao})

    print(livro)
except ValueError as erro:
    print(erro)