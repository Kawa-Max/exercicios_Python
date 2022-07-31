def pontos():
    from time import sleep
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    print()


def linha(tam=42):
    print('', '\033[33m-\033[m' * tam, '')


def leiaInt(num):
    while True:
        try:
            valor = int(input(num))

        except ValueError or TypeError:
            print('\033[31mErro, digite um valor INTEIRO \033[m')

        except KeyboardInterrupt:
            print('\n\033[36mInfelizmente o usuario não quis digitar o valor\033[m')
            break

        else:
            return valor
        break


def titulo(msg):
    linha(42)
    print(f'\033[33m|\033[34m  {msg.center(40)}\033[33m|')
    linha(42)
    print()


def menu(opcoes):
    titulo('Menu Principal')
    i = 1

    print('     ', '\033[33m-\033[m' * 33, '')
    for op in opcoes:
        print(f'\033[33m{"|":>6}\033[93m{i:>4} - \033[94m{op:<25}\033[m\033[33m', f'{"|":>1}')
        i += 1
    print('     ', '\033[33m-\033[m' * 33, '')

    print()
    linha(45)

    opc = leiaInt('\033[33m Qual Opção deseja?\033[m ')

    return opc


def limpaTela(sys):
    import os, time

    time.sleep(0.5)
    return os.system(sys)
