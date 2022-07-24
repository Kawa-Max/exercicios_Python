"""
Crie um programa que faça o computador jogar JOKENPÔ com você.
"""

from time import sleep
from random import randint

pc = randint(1, 3)
print('\033[33m-='*10)
print('\033[7;37m     JO-KEN-PÔ      \033[m')
print('\033[33m-='*10)
sleep(1.5)
print('\033[33m -\033[m'*11)
print('|\033[7;37m    Suas Opções:     \033[m|'
      '\n\033[34m|  [1] - PEDRA        |'
      '\n|  [2] - PAPEL        |'
      '\n|  [3] - TESOURA      |'
      )
print('\033[33m -'*11)
sleep(0.5)
jogador = int(input('\033[37mQual opção deseja: '))
sleep(1)
print('\033[33m-='*14)
print("\033[36m   COMPUTADOR JOGOU ", end='')
if pc == 1:
    print('\033[34mPedra')
elif pc == 2:
    print('\033[34mPapel')
else:
    print('\033[34mTesoura')

print("\033[36m   VOCÊ JOGOU ", end='')
if jogador == 1:
    print('\033[35mPedra')
elif jogador == 2:
    print('\033[35mPapel')
else:
    print('\033[35mTesoura')
print('\033[33m-='*14)
sleep(2)
if jogador == 1:
    if pc == jogador:
        print('\033[33mEMPATE')
    elif pc == 2:
        print('\033[31mVOCÊ PERDEU')
    else:
        print('\033[32mVOCÊ GANHOU')

elif jogador == 2:
    if pc == jogador:
        print('\033[33mEMPATE')
    elif pc == 3:
        print('\033[31mVOCÊ PERDEU')
    else:
        print('\033[32mVOCÊ GANHOU')

elif jogador == 3:
    if pc == jogador:
        print('\033[33mEMPATE')
    elif pc == 1:
        print('\033[31mVOCÊ PERDEU')
    else:
        print('\033[32mVOCÊ GANHOU')

else:
    print('\033[36mValor não reconhecido, mesmo assim.. ', end='')
sleep(0.9)
print('\033[1;30mOBRIGADO POR JOGAR COMIGO')
sleep(0.5)
print('\033[1;31m<<<VOLTE SEMPRE>>>')