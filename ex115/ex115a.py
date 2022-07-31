"""
Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar pessoas pelo seu NOME e IDADE
em um arquivo txt simples

o Sistema só vai ter 2 OPÇÕES: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas

"""

from usaveis import *
from time import sleep

while True:
    limpaTela('cls')
    usuario = menu(['Novo cadastro: ', 'Ver pessoas cadastradas: ', 'Sair do Sistema'])
    if usuario == 1:
        linha(45)
        print('Opc 1'.center(40))
        linha(45)
        sleep(1)

    elif usuario == 2:
        linha(45)
        print('Opc 2'.center(40))
        linha(45)
        sleep(1)

    elif usuario == 3:
        linha(45)
        print('Saindo do sistema, Até logo'.center(40))
        linha(45)
        sleep(1)

        break
    else:
        print('\033[91mErro! Digite uma opção válida!\033[m')

