"""
Faça um programa que mostre a TABUADA de VARIOS NÚMEROS, um de cada vez, para cada
valor digitado pelo usuario. O programa sera INTERROMPIDO quando o valor digitados for negativo
"""
#\033[m
from time import sleep

print('\033[33m -'*9)
print('\033[34m|  T-A-B-U-A-D-A  |')
print('\033[33m -'*9)
sleep(1)

while True:
    n = int(input('\033[37mDigite um valor e veja sua tabuada(N° negativo fecha o programa): '))
    sleep(0.9)

    if n < 1:
        if n == 0:
            print('\033[mValor nulo', end='')
        else:
            print('\033[31mValor negativo\nFechando a T-A-B-U-A-D-A', end='')
        for i in range(0, 4):
            print('\033[34m.', end='')
            sleep(0.5)
        print()
        sleep(1.5)
        break

    print('\033[33mAnalisando o valor digitado \n\033[34m Montando a tabuada', end='')
    for i in range(0, 6):
        print('\033[31m.', end='')
        sleep(0.5)
    print()
    sleep(1.5)

    for c in range(1, 10 + 1):
        print(f'\033[30m|   \033[32m{n}\033[m x \033[35m{c}\033[m = \033[31m{n * c}    \033[30m|')
        sleep(0.7)

print('Obrigado(a) pelo seu tempo ')
print('<<<Volte Sempre>>>')

