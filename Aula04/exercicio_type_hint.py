# Tipe os dados do Desafio da Aula03

while True:
    try:
        nome_usuario: str = str(input("Digite o seu nome: "))
        if nome_usuario.isdigit():
            raise ValueError("Você digitou um número no lugar do nome. Isso não é permitido. ")
        elif len(nome_usuario) == 0:
            raise ValueError("Você não digitou o seu nome e deixou o campo vazio. Isso não é permitido. ")
        elif nome_usuario.isspace():
            raise ValueError("Você digitou apenas espaço em branco no lugar do seu nome. Isso não é permitido. ")
        
        salario_usuario: float = float(input("Digite o seu salário: "))
        bonus_usuario: float = float(input("Digite o valor do bônus que você recebeu (digite somente o número): "))
        
        if not isinstance(salario_usuario, float):
            raise TypeError("Você digitou letras ao invés de número. ")
        elif not isinstance(bonus_usuario, float):
            raise TypeError("Você digitou letras ao invés de número. ")
        
        if salario_usuario >= 0 and bonus_usuario >= 0:
            kpi_bonus: float = float(1000 + (salario_usuario * bonus_usuario))
            print(f"Olá, {nome_usuario}. O seu valor bônus foi de R${kpi_bonus}.")
            exit()
        else:
            print("Você digitou um número negativo para o salário, para o bônus ou para ambos. ")

    except ValueError as erro_valor:
        print(erro_valor)
    except TypeError as erro_tipo:
        print(erro_tipo)