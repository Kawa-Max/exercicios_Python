"""
Faça um MINI-SISTEMA que ultilize o INTERACTIVE HELP do PYTHON.
O usuário vai digitar o comando e o MANUAL ira aparecer. Quando
o usuário digitar a palavra 'FIM' o programa incerrará.

OBS: Use CORES
"""
from time import sleep


def titulo(msg):
    tamanho = len(msg) + 4
    print('\033[96m-' * tamanho)
    print(f'\033[94m  {msg}')
    print('\033[96m-' * tamanho)
    sleep(0.5)


def ajuda(funcao):
    titulo(f'\033[93mAcessando manual de: {funcao} ')
    print('\033[35m')
    help(funcao)
    print('\033[m')
    sleep(0.5)


# Programa Principal
manual = ''
while True:
    titulo('Sistema de ajuda do Max')
    manual = input('\033[32m<<<< Função ou Biblioteca >>> ').strip()
    if manual.upper() == 'FIM':
        break
    else:
        ajuda(manual)

print('\033[35mif precisar:'
      '\n\033[33m    volte'
      '\n\033[35melse:'
      '\n\033[31m    não volte!!!')
