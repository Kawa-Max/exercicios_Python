"""
Crie um programa que tenha uma FUNÇÃO chamada leiaInt(), que vai funcionar
de forma semelhante á função input() do python, só que fazendo a VALIDAÇÃO
para aceitar apenas um valor númerico

ex:

    n = leiaInt('Digite um numero: ')
"""


def leiaInt(num):
    passa = False
    numero = 0
    while True:
        valor = input(num)
        if valor.isnumeric():
            numero = int(valor)
            passa = True
        else:
            print(f'\033[91mError! \033[33mO valor digitado não é um valor inteiro\033[m')
        if passa:
            break
    return numero


n = leiaInt('Digite um numero: ')
print(f'Você digitou o valor {n}')
