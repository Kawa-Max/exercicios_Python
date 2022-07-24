"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e ultimo nome separadamente
ex: Ana Maria Souza
- primeiro = Ana
- segundo = Souza
"""
nome = str(input('\033[31mDigite seu nome completo: ')).split()
print('\033[34mSeu primeiro nome é {}, correto ?\n\033[35me seu ultimo nome é {}..'.format(nome[0], nome[-1]))

