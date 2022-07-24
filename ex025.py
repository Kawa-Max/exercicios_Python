"""
Crie um programa que leia o nome de uma pessoa e diga
se ela tem SILVA no nome
"""
nome = str(input('\033[33mQual seu nome: ')).upper().strip()
print('\033[31m', 'SILVA' in nome)
