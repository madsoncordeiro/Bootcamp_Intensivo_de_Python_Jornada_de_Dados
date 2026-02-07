# 9. Dada uma lista números, extrair apenas aqueles que são pares.

try:
    numeros = input("Digite uma lista de números naturais separados por vírgula (Ex: 1,5,9): ")
    lista_numeros = numeros.split(",")
    numeros_pares = []
    numeros_impares = []

    for numero in lista_numeros:
        if int(numero) % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)

    print(f"""
Números pares:
{numeros_pares}. 
    
Números ímpares:
{numeros_impares}. """)
except ValueError:
    print("Você não digitou a lista de números conforme orientação. ")