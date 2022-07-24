"""
Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados ALEATORIOS.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ORDEM,
sabendo que o VENCEDOR tirou o MAIOR NUMERO no dado
"""
from random import *
from time import sleep
from operator import itemgetter

jogo_dados = dict()

jogo_dados['Kawã'] = randint(1, 6)
jogo_dados['Robert'] = randint(1, 6)
jogo_dados['Carina'] = randint(1, 6)
jogo_dados['Marcos'] = randint(1, 6)
ranking = sorted(jogo_dados.items(), key=itemgetter(1), reverse=True)

print('\033[33mSorteio dados: ')
for k, v in jogo_dados.items():
    print(f'\033[34m{k:<7} \033[91mjogou \033[36m{v:>5}\033[m')
    sleep(0.6)
print(' -' * 20)
print(f'\033[93m{"Ranking dos jogadores":>30}:')
for i, v in enumerate(ranking):
    print(f'\033[96m{i + 1}° lugar: \033[91m{v[0]:<7} com \033[94m{v[1]:>5}')
    sleep(0.7)
