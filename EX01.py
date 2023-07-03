texto = 'exercício 1, cap 03 - quando a máquina começa a tomar decisões'
print('*' * len(texto))
print(texto.upper())
print('*' * len(texto))

print('Nós oferecemos os seguintes planos de assinatura: \n'
      'B - BASIC \n'
      'S - SILVER \n'
      'G - GOLD \n'
      'P - PLATINUM')

basic = 30 / 100
silver = 20 / 100
gold = 10 / 100
platinum = 5 / 100
assinatura = input('Informe a inicial do plano contratado: ').upper()
faturamento = float(input('Qual foi o faturamento anual através do YouTube? R$ '))
if assinatura == 'B':
    bonus = faturamento * basic
elif assinatura == 'S':
    bonus = faturamento * silver
elif assinatura == 'G':
    bonus = faturamento * gold
elif assinatura == 'P':
    bonus = faturamento * platinum
else:
    print('\n\033[31mPLANO DESCONHECIDO!')
    faturamento = 0
    bonus = 0
print('-' * 60)
print(f'O total faturado no ano foi R$ {faturamento:.2f} \n'
      f'Sendo assim, o valor a pagar de bônus é R$ {bonus:.2f}')
print('-' * 60)
