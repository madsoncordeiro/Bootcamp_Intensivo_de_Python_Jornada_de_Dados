# 8. Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
"""
[
    {"nome":"Alice", "email":"alice@example.com"},
    {"nome":"Bob", "email":""},
    {"nome":"Carol", "email":"carol@example.com"}
]
"""

usuarios = [
    {"nome":"Alice", "email":"alice@example.com"},
    {"nome":"Bob", "email":""},
    {"nome":"Carol", "email":"carol@example.com"}
]

usuarios_com_campo_vazio = []
usuarios_com_todos_campos = []

for usuario in usuarios:
    if usuario["nome"] == "" or usuario["email"] == "":
        usuarios_com_campo_vazio.append(usuario)
    else:
        usuarios_com_todos_campos.append(usuario)

print(f"""
Usuários com todos os campos preenchidos:
{usuarios_com_todos_campos}. 
      
Usuários com pelo menos algum campo vazio:
{usuarios_com_campo_vazio}. """)