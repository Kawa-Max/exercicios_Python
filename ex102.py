"""
Crie um programa que tenha uma FUNÇÃO fatorial() que receba dois parametros:
o primeiro que indique o NUMERO a calcular e o outro chamado SHOW, que será
um valor LOGICO(OPCIONAL) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial
"""


def fatorial(num, show=False):
    """

    :param num: Número do fatorial a ser calculado
    :param show: (OPCIONAL) será mostrado ou não o processo de cálculo do fatorial
    :return: Valor do Fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5))
print(fatorial(4, show=True))
help(fatorial)

