# 6. Dada uma lista de e-mails, remover todos os duplicados.

emails:list = ["user@example.com", "admin@example.com", "user@example.com"]
emails_unicos:list = list(set(emails))

print(emails_unicos)