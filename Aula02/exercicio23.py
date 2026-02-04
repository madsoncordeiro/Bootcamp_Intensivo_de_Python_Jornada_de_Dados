# 23. Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /). Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    numero1 = float(input("Digite o primeiro número: "))
    operador = input("Digite qual operação você deseja (utilize o sinal de + para adição, - para subtração, * para multiplicação e / para divisão): ")
    numero2 = float(input("Digite o segundo número: "))
    
    if operador == "+":
        resultado = numero1 + numero2
        print(f"A soma entre {numero1} e {numero2} é igual a {resultado}. ")
    elif operador == "-":
        resultado = numero1 - numero2
        print(f"A subtração entre {numero1} e {numero2} é igual a {resultado}. ")
    elif operador == "*":
        resultado = numero1 * numero2
        print(f"A multiplicação entre {numero1} e {numero2} é igual a {resultado}. ")
    else:
        resultado = numero1 / numero2
        print(f"A divisão entre {numero1} e {numero2} é igual a {resultado}. ")
except ValueError:
    print("Você digitou algo que não é número, número por extenso ou qualquer outro texto. Você precisa digitar somente números quando for solicitado para ser número e somente o sinal da operação desejada quando for solicitado o operador. ")
    
except ZeroDivisionError:
    print("Você tentou dividir um número por zero, o que não é possível. Portanto, digite qualquer número diferente de zero quando for solicitado que digite o segundo número. ")