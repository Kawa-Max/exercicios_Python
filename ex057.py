"""
Faça um programa que leia o SEXO de uma pessoa, mas so aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
"""

s = str(input('Sexo: [M/F] ')).upper()
while s not in 'MmFf':
    s = str(input('\033[31mErro !!\033[m \nDigite seu sexo sendo [M/F]: ')).upper()
print('Sexo {} cadastrado com sucesso'.format(s))



