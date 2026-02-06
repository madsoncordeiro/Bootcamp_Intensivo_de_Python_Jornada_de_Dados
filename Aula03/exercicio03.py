# 3. Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como log = {'timestamp':'2021-06-23 10:00:00', 'level':'ERROR', 'message':'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

registro_log = {'timestamp':'2021-06-23 10:00:00', 'level':'ERROR', 'message':'Falha na conexão'}

level_log = list(registro_log.values())[1]

if level_log == 'ERROR':
    message_log = list(registro_log.values())[2]
    print(message_log)