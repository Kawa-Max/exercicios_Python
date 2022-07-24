"""
Crie um programa que vai ler VARIOS NUMEROS e colocar em uma LISTA

depois disso, mostre:

A) QUANTOS NÚMEROS FORAM DIGITADOS

B) A lista de valores, ordenada de forma DECRESCENTE.

C) Se o valor 5 foi digitado e está ou não na LISTA
"""
num = []

while True:
    num.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar ? [S/N] ').strip().upper()[0]
    while cont not in 'SN':
        cont = input('Quer continuar ? [S/N] ').strip().upper()[0]
    if cont in 'N':
        break

print(f'Você digitou {len(num)} numeros ')
num.sort(reverse=True)
print(f'Sua ordem, DECRESCENTE é :{num}')
if 5 in num:
    print('Valor 5 foi digitado e está na lista')
else:
    print('Valor 5 não foi digitado, e não faz parte da lista')
