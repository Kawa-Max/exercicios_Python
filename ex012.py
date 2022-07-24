"""
faça um algoritmo que leia o preço de um produto
        e
mostre seu novo preço, com 5% de desconto
"""
preco = float(input('\033[7;32mPreço do produto: R$'))
vdesc = preco * 5 / 100
desconto = preco - (preco * 5 / 100)
print('\033[7;31mO produto que custava R${}, com 5% de desconto (R${}),passara a custar R${}'.format(preco, vdesc, desconto))
