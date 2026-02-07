# 13. Simular o consumo de uma API repaginada, onde cada "página" de dados é processada em loop até que não haja mais páginas. 

try:
    pagina_atual = int(input("Digite o número da página atual: "))
    total_paginas = int(input("Digite o número total de páginas: "))

    while pagina_atual <= total_paginas:
        print(f"Página {pagina_atual} de {total_paginas} processada. ")
        pagina_atual += 1
        if pagina_atual == total_paginas:
            print(f"Página {pagina_atual} de {total_paginas} processada. ")
            print(f"Processamento finalizado. ")        
            exit()
except ValueError:
    print("Você digitou algo que não é número. ")