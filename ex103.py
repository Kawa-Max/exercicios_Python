"""
Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois
PARÂMETROS OPCIONAIS: o NOME de um jogador e quantos GOLS ele marcou

Seu programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que
algum dado não tenha sido informado corretamente
"""


def ficha(nome_j='<desconhecido>', gols=0):
    print(f'O jogador {nome_j}, fez {gols} gol(s) no campeonato')


nome = input('Nome do Jogador: ').title().strip()
gol = input('Total de gols: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
