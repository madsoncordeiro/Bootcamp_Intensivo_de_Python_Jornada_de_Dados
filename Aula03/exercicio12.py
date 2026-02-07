# 12. Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

try:
    while True:
        numero_usuario = int(input("Digite um número natural qualquer dentro de uma faixa específica de 0 a 15 para tentar adivinhar qual número fará com que você finalize e saia da execução: "))
        if numero_usuario >= 0 and numero_usuario <= 15:
            if numero_usuario == 10:
                print("Você acertou o número. Até a próxima. ")
                exit()
        else:
            print("Você digitou um número que não está dentro do intervalo específico recomendado. ")
            exit()
except ValueError as erro:
    print("Você não digitou um número. ")