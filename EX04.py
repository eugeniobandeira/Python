texto = 'exercício 4, cap 03 - quando a máquina começa a tomar decisões'
print('*' * len(texto))
print(texto.upper())
print('*' * len(texto))
senha = 'LIBERDADE'
minutos_atuais = int(input('Informe os minutos da hora atual: '))
minuto = minutos_atuais
fatorial = 1
while minuto > 0:
    fatorial *= minuto
    minuto-= 1
print(f'A senha é: {senha+str(fatorial)}')


