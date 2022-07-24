from time import sleep

"""
crie um programa que leia o nome de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- quantas letras ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome
"""
nome = str(input('\033[31mDigite seu nome: '))
nome1 = nome.split()
print('\033[33mNome em analise...')
sleep(1.5)
print('\033[34m----------------------------------------')
print('\033[36mSeu nome em MAIUSCULO é: {}'.format(nome.upper()))
print('\033[34m----------------------------------------')
sleep(1.5)
print('\033[35mSeu nome em minusculo é: {}'.format(nome.lower()))
print('\033[34m----------------------------------------')
sleep(1.5)
print('\033[37mSeu nome tem, ao todo, {} letras(sem contar os espaços)'.format(len(nome.replace(' ', ''))))
# ou tambem
# print('Seu nome tem {} letras '.format(len(nome) - nome.count(' ')))
print('\033[34m----------------------------------------')
sleep(1.5)
# print('Seu primeiro nome {}, tem {} letras'.format(nome1[0], len(nome1[0])))
print('\033[32mSeu primeiro nome tem {} letras '.format(nome.find(' ')))
print('\033[34m----------------------------------------')
sleep(0.9)
print('\033[31mFinalizando a Analise de String')
sleep(2)
