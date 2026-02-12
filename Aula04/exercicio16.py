# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def somar_todos_os_numeros_da_lista_do_usuario(lista_usuario):
    return sum(lista_usuario)

lista_usuario:list = [10.25,20,30,50.25]
soma:float = somar_todos_os_numeros_da_lista_do_usuario(lista_usuario)



print(f"Lista de números: {lista_usuario}. ")
print(f"Soma dos números da lista: {soma}. ")