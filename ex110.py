"""
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
chamada resumo(), que mostre na tela algumas informações geradas pelas
funções que já temos até aqui no modulo criado até aqui
"""

from exercicio107 import moeda

dinheiro = float(input('Digite o valor: R$'))
moeda.resumo(dinheiro, 20, 12)
