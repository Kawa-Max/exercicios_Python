"""
faça um programa que leia um angulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse angulo
"""
from math import tan, sin, cos, radians

angul = int(input('\033[4;30mQual angulo: '))
t = tan(radians(angul))
s = sin(radians(angul))
c = cos(radians(angul))
print('\033[34mO angulo {} tem:\nseno:{:.2f};\ncosseno:{:.2f};\ntangente:{:.2f}'.format(angul, s, c, t))
