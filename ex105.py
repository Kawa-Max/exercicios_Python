"""
Faça um programa que tenha uma FUNÇÃO chamada notas() que pode receber
várias notas de um aluno e vai retornar um DICICONÁRIO com as seguintes
informações:

- QUANTIDADE DE NOTAS
- A MAIOR NOTA
- A MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO (OPCIONAL)

Adicione também as DOCSTRINGS da função

"""

from random import *


def notas(*nota, situ=False):
    """
   :param nota: Notas de um aluno(uma ou varias)
   :param situ: Situação do aluno, opcional
   :return:
   """
    aluno = dict()
    aluno['quantidade'] = len(nota)
    aluno['maior'] = max(nota)
    aluno['menor'] = min(nota)
    media = sum(nota) / len(nota)
    aluno['media'] = f'{media:.2f}'
    if situ:
        if media >= 7:
            aluno['situação'] = 'Aprovado'
        elif media <= 5:
            aluno['situação'] = 'Reprovado'
        else:
            aluno['situação'] = 'Recuperação'
    return aluno


n = notas(randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), situ=True)
print(n)

k = notas(randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10),
          randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), situ=True)
print(k)

o = notas(randrange(0, 10), randrange(0, 10), randrange(0, 10), situ=True)
print(o)
