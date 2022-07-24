"""
Faça um programa que leia um numero inteiro
e diga se ele é ou não um numero primo
"""

digito = int(input('Valor: '))
tot = 0
for c in range(1, digito + 1):
    if digito % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print()
print(f'\033[36mO valor {digito} foi divisivél {tot} vezes, por isso ele ', end='')
if tot == 2:
    print('é PRIMO')
else:
    print('NÃO É PRIMO')
