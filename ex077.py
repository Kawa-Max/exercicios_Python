"""
Crie um programa que tenha uma TUPLA com VARIAS PALAVRAS(não
usa acentos).Depois disso, você deve mostrar, para cada palavra, quais
são sua vogais

"""
from time import sleep

palavras = ('bolsa', 'copo', 'vidro', 'astronauta', 'paquistao')

for palavra in palavras:
    print(f'\033[31mNa palavra \033[33m{palavra}, \033[31msuas vogas são ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print('\033[36m',letra, end=' ')
    print()
    sleep(0.5)
print()
print('\033[35mTeste finalizado')
