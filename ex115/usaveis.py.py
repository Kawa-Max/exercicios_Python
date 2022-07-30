def pontos():
    from time import sleep
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    print()


def linha(tam=42):
    print('\033[33m-\033[m' * tam)


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


def titulo(msg):
    linha(45)
    print(f'\033[34m  {msg.center(40)}')
    linha(45)


def menu(opcoes):
    titulo('Menu Principal')
    i = 1
    for op in opcoes:
        print(f'\033[93m{i} - \033[94m{op}\033[m')
        i += 1
    linha(45)
    opc = leiaInt('\033[33mQual Opção deseja?\033[m ')
    return opc


def limpaTela(sys):
    import os

    return os.system(sys)


