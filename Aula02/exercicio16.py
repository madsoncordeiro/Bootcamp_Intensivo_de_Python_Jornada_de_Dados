# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expressao1 = input("Digite a primeira expressão booleana (True/False): ")
if expressao1 == "True":
    expressao1 = True
elif expressao1 == "False":
    expressao1 = False
else:
    expressao1 = input("Digite a primeira expressão booleana (True/False): ")
expressao2 = input("Digite a segunda expressão booleana (True/False): ")
if expressao2 == "True":
    expressao2 = True
elif expressao2 == "False":
    expressao2 = False
else:
    expressao2 = input("Digite a primeira expressão booleana (True/False): ")
resultado = expressao1 and expressao2

print(f"O resultado da operação 'AND' entre {expressao1} e {expressao2} é {resultado}. ")