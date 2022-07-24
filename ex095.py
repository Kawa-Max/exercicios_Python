from time import sleep

"""
Aprimore o DESAFIO 093 para que ele funcione com VARIOS JOGADORES,
incuindo um sistema de visualização de DETALHES DE APROVEITAMENTO
de cada jogador
"""
jogador = {}
selecao = []
gol = []

while True:
    jogador.clear()

    jogador['nome'] = str(input('\033[93mNome do Atleta: ')).title().strip()
    patidas = int(input(f"\033[33mQuantas partidas {jogador['nome']} fez? "))
    gol.clear()
    for c in range(1, patidas+1):
        gol.append(int(input(f'\033[94m  =>\033[96mQuantos gols na {c}° partida: ')))

    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    selecao.append(jogador.copy())
    continuar = input('\033[92mQuer continuar? [S/N] \033[m').upper()[0].strip()
    while continuar not in 'SsNn':
        print('\033[91mERROOOR !!!\033[m')
        continuar = input('\033[92mQuer continuar? [S/N] \033[m').upper()[0].strip()

    if continuar in 'nN':
        print('Analisando ', end='')
        for i in range(0, 5):
            print('.', end='')
            sleep(0.9)
        print()
        break

print(' -' * 29)
print(f'| {"cod":<4} |', end='')
for k, v in jogador.items():
    print(f' {k:<15}|', end='')
print()
print('_' * 59)
for v, jo in enumerate(selecao):
    print(f'| {v+1:<5}|', end='')
    for j in jo.values():
        print(f' {str(j):<15}|', end='')
    print()

while True:
    levantamento = int(input('Levantamento de qual jogador? (0 para encerrar) '))
    levantamento_jogador = levantamento - 1
    if levantamento < 0:
        print(f'\033[91mPara de ser burro cacete, existe jogador \033[34m{levantamento}\033[91m ai em cima ?\033[m')
        print('<<<NUNCA VOLTE>>>')
        break
    if levantamento == 0:
        break
    if levantamento_jogador >= len(selecao):
        print('\033[31mErro!!\033[m')
    else:
        print(f'     \033[34m==LEVANTAMENTO DE \033[93m{selecao[levantamento_jogador]["nome"]}\033[34m==')
        for jogo, gols in enumerate(selecao[levantamento_jogador]['gols']):
            print(f'     \033[36m--> \033[32mNo jogo \033[31m{jogo+1}\033[32m, fez \033[33m{gols}\033[32m gols\033[m')
    print(' -' * 29)

print('\033[30m<<<ACABOU>>>\033[m')

