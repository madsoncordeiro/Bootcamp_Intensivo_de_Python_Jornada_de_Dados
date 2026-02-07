# 11. Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    dado = input("Digite um dado qualquer (letra, palavra, número etc.). Caso queira finalizar, digite sair: ")
    if dado != "sair":
        print(dado)
    else:
        print(dado)
        exit()