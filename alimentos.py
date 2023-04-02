texto = 'Bem vindo ao EuNutri'
print('*' * 30)
print(texto.upper())
print('*' * 30)
qtd_alimentos = int(input('Quantos alimentos você comeu hoje? '))
print('Quantas calorias cada uma deles tinha? ')
total_calorias = 0
for x in range(1, qtd_alimentos):
    qtd_calorias_uni = float(input(f'Nº de calorias do alimento número {x}: '))
    total_calorias = qtd_calorias_uni + qtd_calorias_uni
print(f'O total de alimentos foi {qtd_alimentos}'
      f'\nA média de calorias foi {total_calorias/qtd_alimentos}')