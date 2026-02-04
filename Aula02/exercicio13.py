# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase_usuario = input("Digite uma frase: ")
frase_usuario = frase_usuario.strip()

print(frase_usuario)