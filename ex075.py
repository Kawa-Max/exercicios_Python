"""
Desenvolva um programa que leia QUATRO VALORES pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9

B) Em que posição foi digitado o primeiro valor 3

C) Quais foram os numeros pares
"""
pares = 0

valores = (int(input('1° valor: ')),
           int(input('2° valor: ')),
           int(input('3° valor: ')),
           int(input('4° valor: '))
           )
print()
print(f'O valor 9 foi digitado {valores.count(9)} vezes ')
if valores.count(3) == 0:
    print('Valor 3 não foi digitado')
else:
    print(f'O primeiro valor 3 foi digitado na {valores.index(3)+1}ª posição')
"""
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na {valores.index(3)+1}° posição')
else:
    print('Valor 3 não foi digitado')
"""

for item in valores:
    if item % 2 == 0:
        pares += 1
if pares == 0:
    print('Nenhum valor par foi digitado')
else:
    print('Os valores pares são: ', end='')
    for valor in valores:
        if valor % 2 == 0:
            print(valor, end=' ')

print()
print('<<<FIM>>>')


