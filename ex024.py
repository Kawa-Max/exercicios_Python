"""
crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com a palavra SANTO
"""
# caso o usuario digitar espaços inuteis, usar o strip()
cidade = str(input('\033[31mQual nome da sua cidade: ')).upper().strip()
print('\033[34mAnalisando se sua cidade começa com Santo:')
print('\033[35m------------------------\n\033[36mTrue = Verdadeiro\nFalse = Falso\n------------------------')
print('\033[32m', cidade[:5] == 'SANTO')
