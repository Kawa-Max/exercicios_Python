"""
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo
com a idade:

- Até 9 ANOS  : MIRIM
- Até 14 ANOS : INFANTIL
- Até 19 ANOS : JUNIOR
- Até 20 ANOS : SÊNIOR
-    Acima    : MASTER
"""

from datetime import datetime
from time import sleep

nascimento = int(input('Ano de nascimento do atleta: '))
sleep(1)
idade = datetime.now().year - nascimento
print()
print('-'*18)
print(f'IDADE: {idade} anos')
print('-'*18)
print()
sleep(1)
if idade <= 9:
    print('Atleta : MIRIM')
elif idade > 9 and idade <= 14:
    print('Atleta : INFANTIL')
elif idade > 14 and idade <= 19:
    print('Atleta : JUNIOR')
elif idade > 19 and idade <= 20:
    print('Atleta : SÊNIOR')
else:
    print('Atleta : MASTER')
print()
sleep(0.5)
