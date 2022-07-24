"""
Escreva um programa que leia um NUMERO N inteiro qualquer e mostre na tela os N
primeiro elementos de uma SEQUENCIA DE FIBONACCI.

Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
from time import sleep



print('\033[33m -'*14)
print('\033[36m|  SEQUÊNCIA DE FIBOACCI    |')
print('\033[33m -'*14)
sleep(0.5)
num = int(input('\033[37mQuantos termos quer mostrar: '))
para = 1
n1 = 0
n2 = 1
soma = 1
sleep(0.2)
print('\033[34mCalculando e montando a sequencia')
sleep(0.9)
while para <= num:
    print('\033[31m',n1, end='\033[32m->\033[m')
    para += 1
    soma = n1 + n2
    n1 = n2
    n2 = soma
    sleep(0.5)
print()
print('\033[35m<<<\033[7;37mFIM DA SEQUÊNCIA DE FIBONACCI\033[m\033[35m>>>\033[m')

