"""
Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a razão de uma PA,  mostrando os 10 PRIMEIROS
TERMOS da progressão usando estrutura WHILE

"""
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
while c <= 10:
    print('{}° termo = {} '.format(c, pt))
    pt = pt + r
    c += 1
print('Fim')
