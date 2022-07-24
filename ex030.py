"""
Crie um programa que leia um numero inteiro e mostre na tela se ele é
PAR ou IMPAR
"""
valor = int(input('\033[34mDigite um valor: '))
if valor % 2 == 0:
    print('\033[31mO valor digitado é par')
else:
    print('\033[32m6O valor digitado é impar')
