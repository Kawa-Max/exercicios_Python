"""
Refaça o DESFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓCELES: dois lados iguais
- ESCALENO: todos os lados diferentes

"""
lado_1 = float(input('Lado 1: '))
lado_2 = float(input('Lado 2: '))
lado_3 = float(input('Lado 3: '))

if lado_1 < lado_2 + lado_3 and \
        lado_2 < lado_1 + lado_3 and\
        lado_3 < lado_2 + lado_1:
    print('É POSSÍVEL FORMAR UM TRIANGULO: ',end='')
    if lado_1 == lado_2 and lado_2 == lado_3:
        print('EQUILÁTERO')
    elif lado_1 != lado_2 != lado_3 != lado_1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('NÃO É POSSIVEL FORMAR UM TRIANGULO')