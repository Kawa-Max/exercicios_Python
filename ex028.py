"""
Escreva um programa que faça o computador "pensar" em um umero inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido
pelo computador

O programa deverá escrever na tela se o usuario venceu ou perdeu
"""
from random import randint

pc = randint(0, 5)
print('\033[36mPensei em um numero entre 0 e 5.')
opc = int(input('\033[35mAdivinhe qual é: \n...'))

print('\033[35mPensei no numero {} e vc no {}.'.format(pc, opc), end=' ')
if opc == pc:
    print('\033[32mParabéns pela vitoria')
else:
    print('\033[31mInfelizmente, voce perdeu')

