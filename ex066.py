"""
Crie um programa que leia VARIOS NUMEROS inteiro pelo teclado.
O programa só vai parar quando o usuario digitar 999, que é a
CONDIÇÃO DE PARADA. No final mostre, QUANTOS NUMEROS foram
digitados e qual foi a SOMA entre eles (desconsiderando o flag)
"""

somatorio = cont = 0
pos = 1

while True:
    numero = int(input(f'\033[32mDigite o {pos}° valor:\033[33m[999 para parar] \033[m'))
    if numero == 999:
        break
    cont += 1
    pos += 1
    somatorio += numero
print(f'\033[35mForam digitados \033[36m{cont}\033[m \033[35mvalores, e a soma de todos é de \033[31m{somatorio}\033[m')
