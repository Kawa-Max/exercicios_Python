"""
Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou. Depois
vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso será
guardado em um dicionario, incluindo o TOTAL DE GOLS feitos durante o campeonato
"""

from time import *

jogador = dict()
gol = []
tot_gol = 0

jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
partida = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(1, partida + 1):
    gols = int(input(f'--> Quantos gols na {c}° partida: '))
    gol.append(gols)
    tot_gol += gols

jogador['gols'] = gol
jogador['total'] = tot_gol
print(' -' * 15)
print(jogador)
print(' -' * 15)

for item, valor in jogador.items():
    print(f'{item} <----> {valor}')
    sleep(0.7)
print(' -' * 15)
print(f"O jogador {jogador['nome']} jogou {partida} partidas")
for p, g in enumerate(gol):
    print(f'    => Na partida {p+1}, marcou {g} gols')
print(f'Foi um total de {jogador["total"]} gols')
