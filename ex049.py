"""
Refaça o DESAFIO 09, mostrando a tabuada de um numero que o usuario escolher,
so que agr usando um LAÇO FOR
"""
from time import sleep

valor = int(input('\033[36mDigite um valor para ver sua tabuada: '))
sleep(0.4)
mult = int(input('\033[31mAté qual valor deseja multiplicar: \033[m'))
sleep(0.5)
print('PROCESSANDO', end='', flush=True)
sleep(0.5)
for i in range(0, 3):
    print('.', end='')
    sleep(0.9)
print()
sleep(0.3)
print('-'*15)
for c in range(0, mult + 1):
    print(f'{valor} x {c} = {valor * c}')
print('-'*15)

