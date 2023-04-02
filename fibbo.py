texto = 'Bem vindo ao E-fibbo'
print('*' * 30)
print(texto.upper())
print('*' * 30)
numero = int(input('Digite um numéro: '))
anterior1 = 1
anterior2 = 0
#0, 1, 1, 2, 3, 5, 8, 13, 21...
for x in range(numero + 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    print(atual)
    if atual == numero:
        print('Ação bem sucedida!')
        break
else:
    print('Ação má sucedida!')

