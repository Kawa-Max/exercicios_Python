"""
Faça um programa que leia um numero de 0 a 9999 e mostre na tela
cada um dos digitos separados
ex:
Digite um valor : 1834
- unidade: 4
- dezena: 3
- centena: 8
- milhar: 1
"""
numero = int(input('\033[34mDigite um valor: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('\033[31munidade:  {}\ndezena:   {}\ncentena:  {}\nmilhar:   {}'.format(u, d, c, m))
