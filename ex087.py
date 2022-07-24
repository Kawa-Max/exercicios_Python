"""
Aprimore o DESAFIO ANTERIOR, mostrando no final:

A) A soma de todos os VALORES pares

B) A soma dos valores da TERCEIRA COLUNA

C) O MAIOR valor da SEGUNDA LINHA

"""
"""
from random import randint

soma_pares = soma_coluna = maior = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        #matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}][{coluna}]: '))
        matriz[linha][coluna] = randint(0, 10)
        print(f'Digite um valor para a posição [{linha}][{coluna}]: {matriz[linha][coluna]}')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
print('-' * 45)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

for linha in range(0, 3):
    soma_coluna += matriz[linha][2]


print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da 2° linha é {max(matriz[1])}')
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        # soma dos valores pares
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')

# soma da terceira coluna
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')
# achando o maior valor da segunda linha
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}')
