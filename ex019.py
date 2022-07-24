"""
Faça um programa que ira sortear quatro alunos para apagar o quadro,
conforme os nomes sejam informados pelo professor e mostre o aluno sorteado
"""
import random
from time import sleep

print('\033[37mSorteio de 4 alunos:')
sleep(2.5)
al1 = str(input('\033[31mNome do 1° aluno: ')).capitalize()
al2 = str(input('Nome do 2° aluno: ')).capitalize()
al3 = str(input('Nome do 3° aluno: ')).capitalize()
al4 = str(input('Nome do 4° aluno: ')).capitalize()
sleep(1)
print('\033[34sorteando...')
sleep(0.9)
lista = [al1, al2, al3, al4]
sorteio = random.choice(lista)
print('\033[32mO aluno sorteado foi: {}'.format(sorteio))
