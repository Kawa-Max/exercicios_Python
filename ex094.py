"""
Crie um programa que leia NOME, SEXO e IDADE de VARIAS PESSOAS, guardando os
dados de cada pessoa em um DICIONARIO e todos os dicionarios em uma lista. No
final, mostre:

A) Quantas pessoas foram cadastradas

B) A MÉDIA de idade do grupo

C) Uma lista com todas as MULHERES

D) Uma lista com todas as pessoas com idade acima da média
"""

from time import *

pessoas = {}
geral = []
media = soma = 0

while True:
    go = input('\033[94mpress GO enter..(S - sair)\033[m').upper().strip()
    while go not in 'GOSgos':
        go = input('\033[96mpress GO enter..(S - sair)\033[m').upper().strip()
    if go in 'GO':
        while True:
            # pedir o nome
            pessoas['nome'] = str(input('Nome: ')).strip().title()
            # pedir o sexo
            pessoas['Sexo'] = str(input('Sexo:[M/F] ')).strip().upper()[0]
            # tratamento de erro
            while pessoas['Sexo'] not in 'MmFf':
                print('\033[91mERROR !!!!\033[m')
                pessoas['Sexo'] = str(input('Sexo:[M/F] ')).strip().upper()[0]
            # pedir idade
            pessoas['idade'] = int(input('Idade: '))
            while pessoas['idade'] > 120 or pessoas['idade'] < 5:
                print('\033[96mIdade Invalida, tente novamente\033[m')
                pessoas['idade'] = int(input('Idade: '))
            soma += pessoas['idade']
            geral.append(pessoas.copy())
            print(' -' * 20)
            continuar = input('Continuar: [S/N] ').upper().strip()[0]
            while continuar not in 'SsnN':
                print('\033[91mERROR !!!!\033[m')
                continuar = input('Continuar: [S/N] ').upper().strip()[0]
            print(' -' * 20)
            if continuar in 'Nn':
                print('Finalizando', end='')
                for c in range(0, 3):
                    print('.', end='')
                    sleep(0.6)
                print()
                break
        break
    elif go in 'sS':
        break
print(' -' * 20)
media = soma / len(geral)
if len(geral) == 1:
    print('Ao todo foram cadastradas, uma pessoa')
elif len(geral) == 0:
    print('Nenhuma pessoa foi cadastrada')
else:
    print(f'Ao todo foram cadastradas, {len(geral)} pessoas')

print()
print(f'A média do grupo é {media:.2f}')
print()
print('A listagem das mulheres é: ')
for pessoa in geral:
    if pessoa['Sexo'] in 'Ff':
        print(f'{pessoa["nome"]} ', end='')
print()
print('As pessoas com idade acima da média são/é: ')
for individuo in geral:
    if individuo['idade'] > media:
        print(f'{individuo["nome"]} ', end='')
print()
