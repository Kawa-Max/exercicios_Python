"""
Crie uma Tupla preencida com os 20 PRIMEIROS colocados da Tabela do CAMPEONATO BRASILEIRO,
na ordem de colocação. Depois mostre:

a)Apenas os 5 PRIMEIROS colocados

b)Os ULTIMOS 4 colocados da tabela

c)Uma lista com os times em ordem alfabetica

d)Em que POSIÇÃO na tabela está o time da CHAPECOENSE
"""
from time import sleep
times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Atlético-MG',
         'Internacional', 'Fluminense', 'Botafogo', 'Santos', 'São Paulo',
         'Bragantino', 'Avaí', 'Atletico-GO', 'Ceará SC', 'Flamengo', 'Coritiba',
         'América-MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')

print('_-' * 20)
print('Times do Brasileirão em ordem de colocação: ')
for time in times:
    print(time, end=', ')
print()
print('_-' * 20)
print(f'Os primeiros colocados são: {times[:5]}')
sleep(0.5)
print('_-' * 20)
print(f'E os 4 ultimos colocados são: {times[-4:]}')
sleep(0.5)
print('_-' * 20)
print(f'Ordem alfabetica dos times: {sorted(times)} ')
sleep(0.5)
print('_-' * 20)

if 'Chapecoense' not in times:
    print('O time da Chapecoense não se encontra na lista')
    sleep(0.5)
else:
    print(f'A Chapecoense se encontra na posição: {times.index("Chapecoense") + 1}')
    sleep(0.5)


