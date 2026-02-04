# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor_usuario = input("Digite um valor booleano (True/False): ")
if valor_usuario == "True":
    valor_usuario = True
elif valor_usuario == "False":
    valor_usuario = False
else:
    valor_usuario = input("Digite um valor booleano (True/False): ")
valor_usuario = not valor_usuario

print(f"O valor booleano invertido ao que você digitou é: {valor_usuario}. ")