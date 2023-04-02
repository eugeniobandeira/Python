import sys
import os
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

print('-' * 30)
print('PROJETO AGêNCIA DE VIAGES')
print('-' * 30)
valor_bruto = float(input('Informe o valor bruto do pacote desejado: '))
print('Qual é a categoria de assento? \n'
                          '1 - Econômica \n'
                          '2 - Executiva \n'
                          '3 - Primeira Classe')
categotia_assento = int(input('Informe a categoria do assento: '))
if categotia_assento < 0 or categotia_assento > 3:
    print('Categoria Inválida!')
    exit()

acompanhantes = int(input('Informe a quantidade de acompanhantes: '))
if categotia_assento == 1 and acompanhantes == 2:
    desconto = valor_bruto * 0.03
elif categotia_assento == 1 and acompanhantes == 3:
    desconto = valor_bruto * 0.04
elif categotia_assento == 1 and acompanhantes >= 4:
    desconto = valor_bruto * 0.05
elif categotia_assento == 2 and acompanhantes == 2:
    desconto = valor_bruto * 0.05
elif categotia_assento == 2 and acompanhantes >= 3:
    desconto = valor_bruto * 0.07
elif categotia_assento == 2 and acompanhantes >= 4:
    desconto = valor_bruto * 0.08
elif categotia_assento == 3 and acompanhantes == 2:
    desconto = valor_bruto * 0.10
elif categotia_assento == 3 and acompanhantes >= 3:
    desconto = valor_bruto * 0.15
elif categotia_assento == 3 and acompanhantes >= 4:
    desconto = valor_bruto * 0.2
else:
    print('Categoria Inválida')
print('*' * 30)
print('RESUMO DO PACOTE')
print(f'Valor bruto R$ {valor_bruto:.2f}')
print(f'Desconto R$ {desconto:.2f}')
print(f'Valor líquido a pagar R$ {(valor_bruto - desconto):.2f}')
print('*' * 30)