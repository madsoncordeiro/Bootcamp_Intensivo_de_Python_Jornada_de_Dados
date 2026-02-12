# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def inverter_string (string_usuario):
    return string_usuario[::-1]

string_usuario: str = input("Digite algo: ")
string_invertida = inverter_string (string_usuario)

print(f"""
O que você digitou: {string_usuario}.
O inverso do que você digitou: {string_invertida}. """)