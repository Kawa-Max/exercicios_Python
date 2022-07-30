"""
Reescreva a função LEIAINT() que fizemos no EX104,
incluindo agr a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie uma
função chamada LEIAFLOAT() com a mesma funcionalidade.
"""


def leiaInt(num):
    while True:
        try:
            valor = int(input(num))

        except ValueError or TypeError:
            print('\033[31mErro, digite um valor INTEIRO \033[m')

        except KeyboardInterrupt:
            print('\033[36mInfelizmente o usuario não quis digitar o valor\033[m')
            break

        else:
            return valor


def leiaFloat(num_real):
    while True:
        try:
            real = float(input(num_real))

        except ValueError or TypeError:
            print('\033[31mErro, digite um valor REAL \033[m')

        except KeyboardInterrupt:
            print('\033[36mInfelizmente o usuario não quis digitar o valor\033[m')
            break

        else:
            return real


numero_inteiro = leiaInt('Digite um valor INTEIRO: ')
numero_real = leiaFloat('Digite um valor REAL: ')

print(f'O valor inteiro digitado foi {numero_inteiro}\nE o real foi {numero_real} ')
