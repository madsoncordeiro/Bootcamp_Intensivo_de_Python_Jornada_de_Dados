# 5. Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$10.000,00 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor':'12000', 'hora':'20'}, verifique se ela é suspeita.

transacao = {'valor':'12000', 'hora':'20'}
valor = float(transacao['valor'])
hora = int(transacao['hora'])

if valor > 10000 or (hora < 9 or hora > 18):
    print("Essa transação é suspeita. ")