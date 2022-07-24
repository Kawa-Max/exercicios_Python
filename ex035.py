"""
Desenvolva um programa que leia o comprimento de tres retas
e diga ao usuario se elas podem ou nao formar um triangulo
"""
print('\033[33m-'*35)
print('\033[36m     Analisador de triangulos')
print('\033[33m-'*35)
l1 = float(input('\033[34mPrimeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('ultimo lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[32mCom essas medidas, é possivel formar um triangulo')
else:
    print('\033[31mAs medidas informadas, não formam um triangulo')
