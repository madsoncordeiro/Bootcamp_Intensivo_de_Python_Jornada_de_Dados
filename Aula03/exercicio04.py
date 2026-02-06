# 4. Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

from email_validator import validate_email, EmailNotValidError

try:
    idade = int(input("Digite a sua idade: "))
    email = input("Digite o seu e-mail: ")

    validacao_email = validate_email(email, check_deliverability=True)
    email = validacao_email.email

    if idade >= 18 and idade <=65:
        print("Dados de usuário válidos. ")
    else:
        print("Idade fora do intervalo permitido. ")
except ValueError as value_error:
    print(value_error)
except email_validator.exceptions.EmailSyntaxError as erro_digitacao_email:
    print(erro_digitacao_email)