"""
Crie um programa que leia NOME e DUAS NOTAS de varias vários alunos
e guarde tudo em uma LISTA COMPOSTA. No final, mostre um BOLETIM contendo
a MÉDIA de cada um e permita que o usuario possa mostrar as NOTAS de cada
aluno individualmente
"""
"""
boletim = []

while True:
    nome = input('Nome do Aluno: ').capitalize().strip()
    nota_1 = float(input('1° nota: '))
    nota_2 = float(input('2° nota: '))
    media = (nota_1 + nota_2) / 2
    boletim.append([nome, [nota_1, nota_2], media])
    continuar = input('Continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SsNn':
        print('\033[91mERRO...\033[m')
        continuar = input('Continuar? [S/N] ').upper().strip()[0]
    if continuar in 'nN':
        break
print(f'{"BOLETIM ESCOLAR":<10}')
print(' =' * 13)
print(f'{"N°":<4}|{"Aluno":<10}|{"Média":<10}|')
print(' =' * 13)
for item, aluno in enumerate(boletim):
    print(f'{item:<4}|{aluno[0]:<10}|{aluno[2]:<10.1f}|')
print()
while True:
    aluno_individual = int(input('Deseja ver a nota de qual aluno ? (-1 para parar)'))
    while aluno_individual > len(boletim):
        print('\033[91mErro.. aluno não encontrado na lista de alunos\033[m')
        aluno_individual = int(input('Deseja ver a nota de qual aluno ? (-1 para parar) '))
    if aluno_individual < 0:
        print('Finalizando ...')
        break
    if aluno_individual <= len(boletim) - 1:
        print(f'As notas do aluno(a) {boletim[aluno_individual][0]} foram {boletim[aluno_individual][1]}')
print('<<<Fim do Boletim>>>')
"""

ficha = []

while True:
    nome = input('Nome: ').capitalize()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8.1f}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno ? (999 interrrompe) '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    print('<<<VOLTE SEMPRE>>>')
