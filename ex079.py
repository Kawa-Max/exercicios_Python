"""
Crie um programa onde o usuario possa digitar varios VALORES NUMERICOS
e cadastre-os em uma LISTA. Caso o numero já exista lá dentro, ele NÃO SERÁ
ADICIONADO. No final, serão exibidos todos os VALORES UNICOS digitados em ORDEM
CRESCENTE
"""

#from random import randint

valores = []

while True:
    valor = int(input('\033[36mValor: '))
    #valor = randint(0, 100)
    #print('\033[36mValor:', valor)
    if valor in valores:
        print('\033[31mErro !! \033[33mNumero repetido, não irei adicionar\033[m')
    else:
        print('\033[32mValor adicionado a lista\033[m')
        valores.append(valor)
    resposta = str(input('\033[34mQuer continuar ?[S/N] ')).strip().upper()[0]
    while resposta not in "SnNs":
        resposta = str(input('\033[31mErro!! \033[34mQuer continuar ?[S/N] ')).strip().upper()[0]
    if resposta in 'nN':
        break

print()
print('\033[33m=-=' * 20)
valores.sort() #colca a lista em ordem
print(f"    \033[35mOs numeros em ordem CRESCENTE é: '\033[30m{valores}\033[35m'")
print('\033[33m=-=' * 20)
