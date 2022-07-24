"""
FAça um programa que jogue PAR OU IMPAR com o computador. O jogo
só será interrompido quando o usuario PERDER, mostrando o total
de vitorias consecultivas que ele conquistou no final do jogo
"""
from random import randint


vitorias = 0

while True:
    jogada = input('Par ou Impar ? ').upper()[0]
    jogador = int(input('Qual numero deseja jogar: '))
    adversario = randint(0, 10)
    print()
    somatorio = adversario + jogador

    if somatorio % 2 == 0:
        final = 'Par'
    elif somatorio %2 == 1:
        final = 'Impar'

    if jogada == 'P':
        opc = 'Par'
        opc_a = 'Impar'
    elif jogada == 'I':
        opc = 'Impar'
        opc_a = 'Par'
    print(f'Sua jogada: N° {jogador} - Opção {opc}'
          f'\nAdversario: N° {adversario} - Opção {opc_a}'
          f'\nResultado: N° {somatorio}, {final}')
    print()
    if somatorio % 2 == 0:
        if jogada in 'P':
            print('vc venceu')
        elif jogada in 'I':
            print('vc perdeu')
            break

    elif somatorio % 2 == 1:
        if jogada in 'P':
            print('vc perdeu')
            break
        elif jogada in 'I':
            print('Vc venceu')
    vitorias += 1
    print()

print(f'Voce venceu {vitorias} vezes consecultivas, Parabens')
print()
print('fim teste')
