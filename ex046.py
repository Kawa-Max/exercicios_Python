"""
Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro
de fogos de artificio, indo de 10 ATE 0, com uma pausa de 1 SEGUNDO entre eles
"""
from time import sleep
import emoji

for c in range(10, 0 - 1, -1):
    if c > 0:
        print(f'{c}-', end='', flush=True)
    elif c == 0:
        print(f'{c} ', end='')
    sleep(0.5)
print(emoji.emojize('\033[31mFELIZ NATAL\033[m:smiley:', language='alias'))
