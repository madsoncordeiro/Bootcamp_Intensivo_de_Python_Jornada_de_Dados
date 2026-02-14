# Refatorar o código do Desafio da Aula03 e usar Dicionário, Type Hint e Funções.

def verificar_se_nome_usuario_esta_dentro_do_esperado(nome_usuario: str = "") -> str:
    while True:
        try:
            nome_usuario: str = input("Digite o seu nome: ")
            if nome_usuario.isdigit():
                raise ValueError("Você digitou um número no lugar do nome. Isso não é permitido. ")
            elif len(nome_usuario) == 0:
                raise ValueError("Você não digitou o seu nome e deixou o campo vazio. Isso não é permitido. ")
            elif nome_usuario.isspace():
                raise ValueError("Você digitou apenas espaço em branco no lugar do seu nome. Isso não é permitido. ")
            else:
                return nome_usuario
        except ValueError as erro:
            print(erro)
            nome_usuario = ""

def calcular_kpi_a_partir_de_salario_e_bonus_usuario_validos(nome_usuario: str, salario_usuario: float = None, bonus_usuario: float = None) -> float:
    while True:
        try:
            salario_usuario: float = float(input("Digite o seu salário: "))
            bonus_usuario: float = float(input("Digite o valor do bônus que você recebeu (digite somente o número): "))
            
            if salario_usuario >= 0 and bonus_usuario >= 0:
                kpi_bonus = 1000 + (salario_usuario * bonus_usuario)
                print(f"Olá, {nome_usuario}. O seu valor bônus foi de R${kpi_bonus}.")
                return kpi_bonus
            else:
                print("Você digitou um número negativo para o salário, para o bônus ou para ambos. ")
                salario_usuario = None
                bonus_usuario = None
        except ValueError:
            print("Digite somente números válidos. ")
 
def executar_informacoes(funcoes: dict) -> None:
    nome = funcoes["nome"]()
    resultado_kpi = funcoes["kpi"](nome)   

informacoes_em_dicionario = {
    "nome": verificar_se_nome_usuario_esta_dentro_do_esperado,
    "kpi": calcular_kpi_a_partir_de_salario_e_bonus_usuario_validos
}

executar_informacoes(informacoes_em_dicionario)