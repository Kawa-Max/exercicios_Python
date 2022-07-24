"""
Faça um programa que tenha uma FUNÇÃO chamada escreva(),
 que receba um texto qualquer como PARÂMETRO e mostre uma
 mensagem com tamanho adaptavél

# EXEMPLO:

# escreva('Olá, Mundo!')

# ~~~~~~~~~~~~~
#  Ola, mundo!
# ~~~~~~~~~~~~~
"""


def escreva(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)


escreva('OLA, MUNDO!')
escreva(input('Digite algo: '))
