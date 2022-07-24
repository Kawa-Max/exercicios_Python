"""
o mesmo professor do ex anterior quer sortear a ordem de apresentaçao
de trabalho dos alunos. Faça um programa que leia o nome dos 4 alunos
e mostre na tela a ordem sorteada
"""
import random

print('\033[31mSorteio de 4 alunos:')
al1 = str(input('Nome do 1° aluno: '))
al2 = str(input('Nome do 2° aluno: '))
al3 = str(input('Nome do 3° aluno: '))
al4 = str(input('Nome do 4° aluno: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('\033[33mA ordem de apresentação será:\n-{} '.format(lista))
