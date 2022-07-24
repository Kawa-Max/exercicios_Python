"""
Melhor o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
O programa encerra, quando ele digitar que quer mostrar 0 termos
"""
from time import sleep


pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
tm = 11
while c < tm:
    print('{}° termo = {} '.format(c, pt))
    pt += r
    c += 1
    if c == tm:
        cont = int(input('Quantos termos a mais deseja mostrar:(0 para parar) '))
        tm += cont
print('Fim')
