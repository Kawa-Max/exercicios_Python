"""
Crie um programa que leia DOIS VALORES e mostre um MENU na tela:

[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS VALORES
[5] - SAIR DO PROGRAMA

Seu programa deverá realizar a operação solicitada em cada caso
"""

valor_1 = int(input('\033[33m1° valor: '))
valor_2 = int(input('2° valor: \033[m'))
esc = 0

while esc != 5:
    print('''\033[36m
      - - - - - - - - - - - - 
    | [1] - SOMAR             |
    | [2] - MULTIPLICAR       |
    | [3] - MAIOR             |
    | [4] - NOVOS VALORES     |
    | [5] - SAIR DO PROGRAMA  |
      - - - - - - - - - - - - 
    \033[m''')
    esc = int(input('\033[37mComo devo prosseguir: '))

    if esc == 1:
        soma = valor_1 + valor_2
        print('\033[32mA soma entre {} e {} resulta em {}'.format(valor_1, valor_2, soma))
    elif esc == 2:
        mult = valor_1 * valor_2
        print('\033[34mA multiplicação entre {} x {} resulta em {}'.format(valor_1, valor_2, mult))
    elif esc == 3:
        if valor_1 > valor_2:
            maior = valor_1
        else:
            maior = valor_2
        print('\033[34mEntre os valores {} e {}, o maior é {}'.format(valor_1, valor_2, maior))
    elif esc == 4:
        print('\033[7;37mDigite os novos valores...\033[m')
        valor_1 = int(input('\033[33m1° valor: '))
        valor_2 = int(input('2° valor: \033[m'))
    elif esc == 5:
        print('\033[1;33mFECHANDO PROGRAMA')
    else:
        print('\033[4;31mValor invalido, tente novamente !!\033[m')
    print('\033[30m-=' * 20)
print('\033[7;37;40m<<<Acabou :)>>>\033[m')