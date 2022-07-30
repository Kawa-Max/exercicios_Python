"""
Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().

Faça também um programa que IMPORT esse módulo e use algumas dessas
funções
"""
from exercicio107 import moeda

# Programa Principal
valor = float(input('Digite o preço: R$'))
print(f'A metade R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}')
print(f'Com aumento de 10%, temos R${moeda.aumentar(valor, 10):.2f}')
print(f'Com diminuição de 10%, temos R${moeda.diminuir(valor, 10):.2f}')
