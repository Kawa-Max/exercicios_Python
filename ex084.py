"""
Faça um programa que leia NOME E PESO de VARIAS PESSOAS, guardando tudo em uma LISTA.
no final mostre:

A) QUANTAS pessoas foram cadastradas

B) Uma listagem com as mais PESADAS

C) Uma listagem com as pessoas mais LEVES
"""
"""
pessoal = []
individuo = []
maior_peso = menor_peso = 0
c = 1
while True:
    print(' -' * 9)
    print(f'|    {c}° pessoa    |')
    print(' -' * 9)
    c += 1
    individuo.append(input('Nome: '))
    individuo.append(float(input(f'Peso: ')))
    if len(pessoal) == 0:
        maior_peso = menor_peso = individuo[1]
    else:
        if individuo[1] > maior_peso:
            maior_peso = individuo[1]
        if individuo[1] < menor_peso:
            menor_peso = individuo[1]
    pessoal.append(individuo[:])
    individuo.clear()
    print('=-=' * 10)
    continuar = input('Deseja cadastrar mais alguém ? [S/N] ').strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = input('\033[91mErro..\033[mDeseja cadastrar mais alguém ? [S/N] ').strip().upper()[0]
    print('=-=' * 10)
    if continuar in 'Nn':
        break

print()
print(f'\033[91mForam cadatradas \033[90m{len(pessoal)} \033[91mpessoas')
print()
print('\033[32mO maior peso lido foi de \033[96m', end='')
for p in pessoal:
    if p[1] == maior_peso:
        print(p[0], end=', ')
print(f'\033[m pesando \033[37m{maior_peso}')
print()
print(f'\033[32mE o menor peso foi de \033[94m', end='')
for p in pessoal:
    if p[1] == menor_peso:
        print(p[0], end=', ')
print(f'\033[m pesando \033[35m{menor_peso}')
print()

"""

# correção Curso em Video

temp = []
princ = []
mai = men = 0

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continuar [S/N] ')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('\033[31mContinuar [S/N] \033[m')).upper().strip()[0]

    if resp in 'Nn':
        break
print('=-=' * 40)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso lido foi {mai}kg, de ', end='')
for pessoa in princ:
    if pessoa[1] == mai:
        print(f'[{pessoa[0]}] - ', end='')
print()

print(f'O menor peso lido foi {men}kg, de ', end='')
for pessoa in princ:
    if pessoa[1] == men:
        print(f'[{pessoa[0]}] - ', end='')
print()

