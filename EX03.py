texto = 'exercício 3, cap 03 - quando a máquina começa a tomar decisões'
print('*' * len(texto))
print(texto.upper())
print('*' * len(texto))
soma_nota_impar = 0
soma_nota_par = 0
total_alunos_turma = int(input('Informe a quantidade de alunos na turma: '))
media_turma = total_alunos_turma / 2

#IMPAR
for aluno in range(1, total_alunos_turma + 1):
    if aluno % 2 == 1:
        aluno_impar_nota = float(input(f'Você está digitando as notas dos alunos ímpares, '
                                       f'por favor, informe a nota aluno nº {aluno}: '))
        if aluno_impar_nota < 0 or aluno_impar_nota > 10:
            aluno_impar_nota = 0
        soma_nota_impar = soma_nota_impar + aluno_impar_nota
media_impar = soma_nota_impar / media_turma

#PAR
for aluno in range(1, total_alunos_turma + 1):
    if aluno % 2 == 0:
        aluno_par_nota = float(input(f'Você está digitando as notas dos alunos pares, por favor, '
                                     f'informe a nota aluno nº {aluno}: '))
        if aluno_par_nota < 0 or aluno_par_nota > 10:
            aluno_par_nota = 0
        soma_nota_par = soma_nota_par + aluno_par_nota
media_par = soma_nota_par / media_turma

print('*' * 60)
print(f'A somatória das notas dos alunos impares foi {soma_nota_impar:.2f}. A média foi {media_impar:.2f}')
print('*' * 60)
print(f'A somatória das notas dos alunos pares foi {soma_nota_par:.2f}. A média foi {media_par:.2f}')
print('*' * 60)
if media_impar > media_par:
    print('A turma de números IMPARES teve a maior média')
elif media_par > media_impar:
    print('A turma de números PARES teve a maior média')
else:
    print('A média tanto ímpar como par teve o valor igual')
print('*' * 60)
