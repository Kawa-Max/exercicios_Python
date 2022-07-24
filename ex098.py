"""
Faça um programa que tenha uma FUNÇÃO chamada contador(),
que receba três PARÂMETROS;INICIO, FIM, PASSO e realize
a contagem seu programa tem que realizar TRES CONTAGENS atraves da
função criada:

A) De 1 até 10, de 1 em 1

B) De 10 até 0, de 2 em 2

C) Uma contagem PERSONALIZADA
"""
from time import sleep


def contador(ini, fim, pas):
    if pas == 0:
        pas = 1
    if pas < 0:
        pas *= -1

    print(f'Contando de {ini} até {fim} indo de {pas} em {pas}')
    cont = ini
    if ini < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += pas
            sleep(0.5)
        print()
    else:
        while fim <= cont:
            print(f'{cont} ', end='')
            cont -= pas
            sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
