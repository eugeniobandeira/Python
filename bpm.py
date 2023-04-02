idade = int(input('Informe sua idade: '))
batimentos_por_minuto = int(input('Informe os seus batimentos por minuto: '))

#até 2 anos de idade
if idade <= 2 and (batimentos_por_minuto >= 120 and batimentos_por_minuto <= 140):
    print(f'Ok, seus BPMs {batimentos_por_minuto} estão dentro da faixa adequada [120 a 140]')
elif idade <= 2 and batimentos_por_minuto < 120:
    print(f'Seus BPMs {batimentos_por_minuto} estão ABAIXO da faxia adequada [120 a 140]')
elif idade <= 2 and batimentos_por_minuto > 140:
    print(f'Seus BPMs {batimentos_por_minuto} estão ACIMA da faxia adequada [120 a 140]')
#de 8 até 17 anos
elif (idade > 2 and idade <= 17) and (batimentos_por_minuto >= 80 and batimentos_por_minuto <= 100):
    print(f'Ok, seus batimentos {batimentos_por_minuto} estão dentro da faixa adequada [80 a 100]')
elif (idade > 2 and idade <= 17) and batimentos_por_minuto < 80:
    print(f'Seus BPMs {batimentos_por_minuto} estão ABAIXO da faxia adequada [80 a 100]')
elif (idade > 2 and idade <= 17) and batimentos_por_minuto > 100:
    print(f'Seus BPMs {batimentos_por_minuto} estão ACIMA da faxia adequada [80 a 100]')
#adulto
elif (idade > 17 and idade <= 50) and (batimentos_por_minuto >= 70 and batimentos_por_minuto <= 80):
    print(f'Ok, seus batimentos {batimentos_por_minuto} estão dentro da faixa adequada [70 a 80]')
elif (idade > 17 and idade <= 50) and batimentos_por_minuto < 70:
    print(f'Seus BPMs {batimentos_por_minuto} estão ABAIXO da faxia adequada [70 a 80]')
elif (idade > 17 and idade <= 50) and batimentos_por_minuto > 80:
    print(f'Seus BPMs {batimentos_por_minuto} estão ACIMA da faxia adequada [70 a 80]')
#idoso
elif idade > 50 and (batimentos_por_minuto >= 50 and batimentos_por_minuto <= 60):
    print(f'Ok, seus batimentos {batimentos_por_minuto} estão dentro da faixa adequada [50 a 60]')
elif idade > 50 and batimentos_por_minuto < 50:
    print(f'Seus BPMs {batimentos_por_minuto} estão ABAIXO da faxia adequada [50 a 60]')
elif idade > 50 and batimentos_por_minuto > 60:
    print(f'Seus BPMs {batimentos_por_minuto} estão ACIMA da faxia adequada [50 a 60]')
else:
    print('Dados inválidos!')
