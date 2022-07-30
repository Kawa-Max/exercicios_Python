"""
Crie um código em Python que teste se o site
PUDIM está acessível pelo computador usado
"""

import requests


def pontos():
    from time import sleep
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    print()


print('tentando acessar o site desejado ', end='')
pontos()

site_pudimzinho = 'http://www.pudim.com.br/'

try:
    acesso = requests.get(site_pudimzinho)

except:
    print('\033[91mNão foi possivel acessar o site desejado\033[m')

else:
    print('\033[32mAcesso efetuado com sucesso\033[m')
