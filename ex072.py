"""
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de ZERO até VINTE

Seu programa deverá ler um numer pelo teclado (entre 0 e 20)
e mostra-lo por EXTENSO
"""
cor = ('\033[m',
       '\033[30;44m',
       '\033[31m',
       '\033[33m',
       '\033[36m'
       )
extenso_num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('\033[34mDigite um valor entre 0 e 20 e veja seu extensivo: '))
while numero < 0 or numero > 20:
    print('\033[31mERROR ...', end='')
    if numero < 0:
        print('\033[33mNumero menor que 0')
    elif numero > 20:
        print('\033[36mNumero acima de 20')
    numero = int(input('\033[34mDigite apenas valores entre 0 e 20: '))

print(f'\033[35mO extensivo de \033[32m{numero}\033[m\033[35m, é {cor[1]}{extenso_num[numero]}{cor[0]}')
