"""
Faça um programa que leia algo peo teclado e mostre
na tela seu tipo primitivo e todas informações sobre ele
"""
a = input('\033[33mDigite algo: ')
print('\033[37m', type(a))
print('\033[32mÉ NUMERICO: ',a.isnumeric())
print('É ALFABETICO: ',a.isalpha())
print('É ALFANUMERICO: ',a.isalnum())
print('ESTÁ TUDO EM MAIUSCULO: ',a.isupper())
print('ESTÁ TUDO EM MINUSCULO: ',a.islower())
print('SO TEM ESPAÇOS: ',a.isspace(),'\033[m')
