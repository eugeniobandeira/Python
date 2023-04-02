texto = 'Sorteio de Video Game'
print('*' * len(texto))
print(texto)
print('*' * len(texto))
print('Temos as seguintes opções: \n 1 - PLAYSTATION \n 2 - XBOX \n 3 - NINTENDO')
playstation = 0
xbox = 0
nintendo = 0
colaborador1 = input('Insira o seu voto: ')
colaborador2 = input('Insira o seu voto: ')
colaborador3 = input('Insira o seu voto: ')
colaborador4 = input('Insira o seu voto: ')
colaborador5 = input('Insira o seu voto: ')
if colaborador1 == '1':
    playstation = playstation + 1
elif colaborador1 == '2':
    xbox = xbox + 1
elif colaborador1 == '3':
    nintendo = nintendo + 1
if colaborador2 == '1':
    playstation = playstation + 1
elif colaborador2 == '2':
    xbox = xbox + 1
elif colaborador2 == '3':
    nintendo = nintendo + 1
if colaborador3 == '1':
    playstation = playstation + 1
elif colaborador3 == '2':
    xbox = xbox + 1
elif colaborador3 == '3':
    nintendo = nintendo + 1
if colaborador4 == '1':
    playstation = playstation + 1
elif colaborador4 == '2':
    xbox = xbox + 1
elif colaborador4 == '3':
    nintendo = nintendo + 1
if colaborador5 == '1':
    playstation = playstation + 1
elif colaborador5 == '2':
    xbox = xbox + 1
elif colaborador5 == '3':
    nintendo = nintendo + 1
else:
    print('Voto inválido!')
print('Segue a análise dos votos')
print(f'Playstation: {playstation}')
print(f'Xbox: {xbox}')
print(f'Nintendo: {nintendo}')
