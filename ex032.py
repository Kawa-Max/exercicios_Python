"""
Faça um programa que leia um um ano e mostre se ele é BISSEXTO
"""
from datetime import date

ano = int(input('\033[35mQual ano deseja analisar: 0 para analisar se o ano atual é bissesto\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano de {}, é BISSEXTO'.format(ano))
else:
    print('\033[31mO ano de {}, não é BISSEXTO'.format(ano))
