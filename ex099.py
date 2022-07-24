"""
Faça um programa que tenha uma FUNÇÃO chamada maior, que receba
vários PARÂMETROS com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o MAIOR
"""
from random import randint


def maior(*num):
    mai = 0
    cont = 0
    for numero in num:
        if cont == 0:
            mai = numero
        else:
            if numero > mai:
                mai = numero
        cont += 1
    print(f'\033[93mDentre os valores \033[94m{num}\033[93m, o maior valor lido foi \033[96m{mai}')


maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
