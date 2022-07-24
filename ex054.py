"""
Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
No final, mostre:
quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores
"""
from datetime import datetime
from random import randint

m_i = mn_i = 0

for c in range(1, 7+1):
    nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = datetime.now().year - nasc
    if idade >= 18:
        m_i +=1
    else:
        mn_i += 1

print(f'Ao todo, {m_i} pessoas são maiores de idade ')
print(f'E {mn_i} são menores de idade')

