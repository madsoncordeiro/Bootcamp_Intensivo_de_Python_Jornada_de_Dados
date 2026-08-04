nome_aluno: str = 3

# isinstance verifica se a instância está dentro da classe que você fez
if isinstance(nome_aluno, str):
    nome_aluno_maiusculo = nome_aluno.upper()
    print(nome_aluno_maiusculo)

else:
    print("Você digitou uma classe errada. Precisa ser string. ")
