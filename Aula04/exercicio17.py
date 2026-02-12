# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def verificar_se_numero_e_primo(numero: int) -> bool:
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    
    limite: int = int(numero ** 0.5) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True

numero:int = int(7)
e_primo = verificar_se_numero_e_primo(numero)

print(f"O número {numero} é primo: {e_primo}. ")