"""
Crie um programa que leia uma FRASE qualquer e diga
se ela é ou não um PALÍNDROMO, desconsiderandos espaços

palindromo == frase dita igualmente de frente para tras, e de tras para frente

ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA

"""

frase = str(input('Digite algo: ')).upper().strip().split()
juntar = ''.join(frase)
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]
print(f'\033[36m{juntar} - \033[31m{inverso}\033[m')
if inverso == juntar:
    print('\033[34mTemos um palídromo')
else:
    print('\033[33mA frase digitada não forma um palíndromo ')

