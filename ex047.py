"""
Crie um programa que mostre na tela TODOS OS NUMERS PARES
que estão no intervalor entre 1 e 50
"""
from time import sleep

for c in range(1, 50+2):
    if c % 2 == 0:
        print(c)
        sleep(0.5)

for n in range(2, 51, 2):
    print(n, end=' ')