"""
Faça um programa que leia 3 numeros e mostre
qual é o maior
      e
qual é o menor
"""

pn = int(input('\033[34mPrimeiro valor: '))
sn = int(input('Segundo valor: '))
tn = int(input('Terceiro valor: '))
#encontrando o maior
maior = pn
if sn > pn and sn > tn:
    maior = sn
if tn > pn and tn > sn:
    maior = tn

#encontrando o menor
menor = pn
if sn < pn and sn < tn:
    menor = sn
if tn < pn and tn < sn:
    menor = tn

print('\033[31mO maior valor digitado foi {}'.format(maior))
print('\033[32mO menor valor digitado foi {}'.format(menor))
