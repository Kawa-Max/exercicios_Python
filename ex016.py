"""
Crie um programa que leia um valor Real qualquer pelo teclado
e mostre sua porcao inteira

ex:
digite um numero: 6.127
O numero 6.127 tem a parte inteira 6
"""
from math import trunc

valor_R = float(input('\033[31mDigite um valor Real: '))
# print('a pocao inteira equivale a {:.0f}'.format(valor_R))
print('\033[33mA porcao inteira de {} e {}'.format(valor_R, trunc(valor_R)))
