"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
"""
from time import sleep

co = float(input('\033[33mDigite o valor do cateto oposto: '))
ca = float(input('Digite o valor do caeto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('\033[34mCalculando a hipotenusa..')
sleep(0.9)
print('\033[32mA hipotenusa vale {:.2f}'.format(hi))
