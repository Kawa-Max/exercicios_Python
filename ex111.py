"""
Crie um PACOTE chamado utilidadesCeV que tenha dois MODULOS INTERNOS
chamados MOEDA e DADO.

Transfira todas as funções ultilizadas nos DESAFIOS 107, 108, 109 e 110
para o primeiro pacote e mantenha tudo funcionando

"""

from utilidadesCeV import moeda

grana = float(input('Valor: R$'))
moeda.resumo(grana, 75, 59)
