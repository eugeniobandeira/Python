texto = 'Bem vindo ao E-transações'
print('*' * 30)
print(texto.upper())
print('*' * 30)
transacoes = int(input('Quantas transações você realizou hoje? '))
valor_gasto = 0
for x in range(1, transacoes+1):
    valor_por_transacao = float(input(f'Valor gasto na transação {x}: '))
    valor_gasto = valor_por_transacao + valor_gasto
print(f'Total gasto no dia R$ {valor_gasto}')