"""
Faça um programa que tenha uma LISTA chamada NUMEROS e duas funções
chamadas sorteia() e somaPar(). A primeira vai sortear 5 NUMEROS
ALEATORIOS e vai coloca-los dentro da lista e a segunda função vai
mostrar a SOMA entre todos os valores PARES sorteados pela função
anterior
"""
from random import randint

numeros = list()


def sorteia():
    print('\033[93mValores Sorteados: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'\033[92m{numeros} ', end='')
    print('\033[33mPronto')


def somaPar():
    sorteia()
    soma_p = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma_p += valor

    print(f'\033[95mA soma entre os valores pares é: \033[96m{soma_p}')


somaPar()
