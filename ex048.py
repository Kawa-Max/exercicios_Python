"""
Faça um programa que calcule a
 entre todos os NUMEROS IMPARES
que são MULTIPLOS DE TRES e que se encontram no intervalo de 1 até 500
"""

s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma entre os {cont} valores multiplos de 3, entre 1 e 500, é {s}')
