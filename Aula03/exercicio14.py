# 14. Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

try:
    limite_tentativas = int(input("Digite qual é o número máximo de tentativas de reconexão ao serviço: "))
    tentativa = 1

    while tentativa <= limite_tentativas:
        print(f"Tentando reconexão ao serviço... ({tentativa} de {limite_tentativas}) ")
        tentativa += 1
        if tentativa == limite_tentativas:
            print(f"Tentando reconexão ao serviço... ({tentativa} de {limite_tentativas}) ")
            print("O número máximo de tentativas de reconexão ao serviço foi atingido. ")
            exit()
except ValueError:
    print("Você não digitou um número. ")