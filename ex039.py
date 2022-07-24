"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele AINDA VAI SE ALISTAR ao serviço militar
- Se é a HORA DE SE ALISTAR
- Se já PASSOU DO TEMPO do alistamento

Seu programa deverá mostrar o tempo que falta ou que passou do prazo

"""
from time import sleep
from datetime import datetime
print('\033[33m-'*15)
print('\033[35m  ALISTAMENTO')
print('\033[33m-\033[m'*15)
print()
sleep(0.9)
nasc = int(input('\033[4;37mQual seu ano de nascimento? \033[m'))
idade = datetime.now().year - nasc
print()
sleep(1)
print('\033[33m-'*18)
print(f'\033[37m IDADE: {idade} anos')
print('\033[33m-'*18)
print()
sleep(0.9)
if idade < 18:
    falta =  18 - idade
    if falta == 1:
        print(f'\033[32mVocê ainda irá se alista daqui {falta} ano ')
        sleep(2)
    else:
        print(f'\033[32mVocê ainda irá se alista daqui {falta} anos ')
        sleep(2)
elif idade == 18:
    print('\033[31mCORRA!! Está na hora de se alistar ')
    sleep(2)
else:
    passou = idade - 18
    print(f'\033[33mSeu prazo de alistamento passou ja faz {passou} anos')
    sleep(2)

