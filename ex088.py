"""
Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES.
O programa vai perguntar QUANTOS JOGOS serão gerados e vai sortear 6 NÚMEROS
ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA
"""
from random import randint
from time import sleep

"""
print('=' * 25)
print('\033[33m{:>20}\033[m'.format('Jogo Mega-Sena'))
print('=' * 25)
print()

jogo = []
palpites = []
c = 1
quant = int(input('\033[94mQuantos jogos serão sorteados: \033[m'))
print()
for p in range(0, quant):
    valores = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    palpites.append(valores[:])

for palpite in palpites:
    print(f'\033[95mJogo {c}: \033[36m{palpite}')
    c += 1
    sleep(0.5)
print()
print('\033[33m<<<\033[91mBoa Sorte Calango\033[33m>>>')
"""

print('', '\033[93m-' * 30)
print('\033[93m|     \033[33mJOGA NA MEGA SENA         \033[93m|')
print('', '\033[93m-' * 30)
quant = int(input('\033[35mQuantos jogos você quer que eu sorteie: '))

lista = []
jogos = []

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('\033[93m-=' * 3, f' \033[96mSORTEANDO \033[91m{quant} \033[96mJOGOS ', '\033[93m-=' * 3)
for i, l in enumerate(jogos):
    print(f'\033[94mJogo \033[90m{i+1}: \033[97m{l}')
    sleep(0.7)

print()
print('\033[93m-=' * 5, '\033[30m<Boa Sorte>', '\033[93m-=' * 5)
