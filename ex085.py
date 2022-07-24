"""
Crie um programa onde o usuario possa digitar SETE VALORES NÚMERICOS
e cadastre-os em uma LISTA UNICA que mantenha separados os valores
PARES e IMPARES. No final, mostre os valores pares e impares em ordem
CRESCENTE
"""
from time import sleep
from random import randint, choice

"""
pain = [[], []]
print('\033[91mDigite 7 valores inteiros, por favor')
for c in range(1, 7+1):
    numero = int(input(f'\033[32m{c}° valor: '))
    #numero = randint(0, 1000)
    #print(f'\033[32m{c}° valor: {numero}')
    sleep(0.5)
    if numero % 2 == 0:
        pain[1].append(numero)
    elif numero % 2 == 1:
        pain[0].append(numero)

print()
pain[0].sort()
print(f'\033[36mOs valores impares: \033[90m{pain[0]}')
print()
pain[1].sort()
print(f'\033[95mOs valores pares: \033[33m{pain[1]}')
print()

"""

# Correção Curso em Video

cores = ('\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[30m')
num = [[], []]
valor = 0

for c in range(1, 7+1):
    valor = int(input(f'{choice(cores)}Digite o {c}o. valor: \033[m'))
    #sleep(0.2)
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'\033[31mOs valores \033[94mpares\033[m \033[31mdigitados foram: \033[36m {num[0]}\033[m')
print(f'\033[31mos valores \033[96mimpares\033[m \033[31mdigitados foram: \033[34m {num[1]}\033[m')
