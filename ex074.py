"""
Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA

Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MAIOR e o MENOR
valor que estão na tupla
"""
from random import randint
from time import sleep

valores = (randint(0,10), randint(0, 9), randint(0, 7), randint(0,12), randint(0, 5))

print('Os valores gerados foram: ', end='')
for n in valores:
    print(f'{n} ', end='')
print()
print(f'O maior valor foi {max(valores)}')
print(f'O menor valor foi {min(valores)}')

