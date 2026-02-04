# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
data_usuario = data_usuario.split("/")

print(f"A data que você digitou corresponde ao dia {data_usuario[0]}, mês {data_usuario[1]} e ao ano {data_usuario[2]}. ")