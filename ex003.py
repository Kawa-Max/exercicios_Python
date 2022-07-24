"""
Crie um programa que leia dois numeros e tente mostrar a soma entre eles
"""
n1 = int(input('\033[33mDigite um valor: '))
n2 = int(input('Digite outro valor: \033[m'))
s = n1 + n2
print('\033[35mA soma entre {} + {} é igual {}'. format(n1, n2, s))
