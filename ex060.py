"""
Faça um programa que leia um NUMERO qualquer e mostre o seu FATORIAL

ex:

5! = 5x4x3x2x1 = 120
"""
from time import sleep


n = int(input('Digite um valor e veja seu FATORIAL: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
sleep(0.9)

while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
        sleep(0.5)
    else:
        print(' = ', end='')
        sleep(0.5)
    f *= c
    c -= 1
print('{}'.format(f))

