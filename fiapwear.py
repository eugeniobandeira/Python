valorCompra = input('Informe o valor da compra: ')
cupom = input('informe o cupom de desconto: ').upper()
if cupom == "NIVER10":
    valorCompra = float(valorCompra) * 0.9
print(f'Total a pagar R$ {valorCompra:.2f}')
