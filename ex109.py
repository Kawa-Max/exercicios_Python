"""
Modifique as funções que foram criadas no ex107 para que elas
aceitem UM PARÂMETRO  a mais, informando se o valor retornado
por elas vai ser ou não formatado pela função moeda()
desenvolvida no ex108
"""
from exercicio107 import moeda

# Programa Principal
valor = float(input('Digite o preço: R$'))
print(f'\033[94mA metade {moeda.moeda(valor)} \033[94mé {moeda.metade(valor, True)}')
print(f'\033[94mO dobro de {moeda.moeda(valor)} \033[94mé {moeda.dobro(valor, True)}')
print(f'\033[94mCom aumento de \033[96m10%\033[94m, temos {moeda.aumentar(valor, 10, True)}')
print(f'\033[94mCom diminuição de \033[96m10%\033[94m, temos {moeda.diminuir(valor, 13, True)}')
