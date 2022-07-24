"""
Desenvolva um programa que leia o 1° TERMO de uma PA. No final,
mostre os 10 primeiros termos dessa progressão
"""

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dez = pt + (10 - 1) * r
for c in range(pt, dez + r, r):
    print(c, end=' -> ')
print('Fim')


