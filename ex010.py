"""
crie um programa que leia quanto de reais uma pessoa tem na carteira
                e
mostre quantos dolar ela pode comprar

CONSIDERE:
US$1 = 4.75
"""
carteira = float(input('\033[33mQual valor em R$ vc tem na carteira: R$'))
dolar = carteira / 4.75
euro = carteira / 5.12
print('\033[32mCom R${}, voce pode comprar:\nUS${:.2f};\n£{:.2f}'.format(carteira, dolar, euro))
