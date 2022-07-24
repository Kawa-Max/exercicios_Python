"""
Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3
e preencha com valores lidos pelo teclado

No final, mostre a MATRIZ na tela, com a formatação correta
"""
"""
from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}][{coluna}]: '))
        #matriz[linha][coluna] = randint(0, 500)
        #print(f'Digite um valor para a posição [{linha}][{coluna}]: {matriz[linha][coluna]}')
print('-' * 45)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
