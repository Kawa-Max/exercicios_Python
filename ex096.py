"""
Faça um programa que tenha uma FUNÇÃO chamada área(),
que receba as dimensões de um terreto retangular (largura
e comprimento) e mostre a AREA DESSE TERRENO
"""


def área(largura, comprimento):
    area = largura * comprimento
    print(f'Com as dimensões {largura}x{comprimento} a área desse terreno é {area}m²')


print('Controle de Terreno')
print('-' * 20)
larg = float(input('Largura (m): '))
compri = float(input('Comprimento (m): '))
área(larg, compri)
