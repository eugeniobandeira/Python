texto = 'exercício 2, cap 03 - quando a máquina começa a tomar decisões'
print('*' * len(texto))
print(texto.upper())
print('*' * len(texto))
print('Precisamos definir qual é o melhor dia para realizar a nossa live semanal.\n'
      'Para começarmos..')
qtd_alunos = int(input('Informe a quantidade de alunos que há na turma: '))
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
nulo = 0
print('Temos as seguintes opções: \n'
      '1 - Segunda Feira\n'
      '2 - Terça Feira\n'
      '3 - Quarta Feira\n'
      '4 - Quinta Feira\n'
      '5 - Sexta Feira')
for voto in range(1, qtd_alunos + 1):
    escolha = int(input(f'Voto nº {voto}: '))
    if escolha == 1:
        segunda += 1
    elif escolha == 2:
        terca += 1
    elif escolha == 3:
        quarta += 1
    elif escolha == 4:
        quinta += 1
    elif escolha == 5:
        sexta += 1
    else:
        nulo += 1

print(f'Total de Votos\n'
    f'Segunda Feira: {segunda}\n'
    f'Terça Feira: {terca}\n'
    f'Quarta Feira: {quarta}\n'
    f'Quinta Feira: {quinta}\n'
    f'Sexta Feira: {sexta}\n'
    f'Nulos: {nulo}')

print('-' * 110)
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta and segunda > nulo:
    print(f'O dia definido para termos lives foi segunda, com o total de {segunda} votos')
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta and terca > nulo:
    print(f'O dia definido para termos lives foi terça, com o total de {terca} votos')
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta and quarta > nulo:
    print(f'O dia definido para termos lives foi quarta, com o total de {quarta} votos')
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta and quinta > nulo:
    print(f'O dia definido para termos lives foi quinta, com o total de {quinta} votos')
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta and sexta > nulo:
    print(f'O dia definido para termos lives foi sexta, com o total de {sexta} votos')
elif nulo > segunda and nulo > terca and nulo > quarta and nulo > quinta and nulo > sexta:
    print(f'Não foi possível chegar a um consenso, pois houve mais votos nulos do que úteis para escolher o dia de live')
else:
    print('Não foi possível chegar a um acordo, pois houve um empate')
print('-' * 110)
