valor = float(input('Digite o valor da compra: '))
meioPagamento = input('Informe o método de pagamento D-DINHEIRO C-CARTAO ').upper()
if valor > 100 or meioPagamento == "D":
    print('Você receberá 10% de desconto sobre {}'.format(valor))
    print('Total a pagar R$ {}'.format(valor * 0.9))
else:
    print('Não é possível conceder desconto nessa operação')