"""
Adapte o código do ex107, criando uma função adicional
chamada moeda() que consiga mostrar os valores como um valor
monetário formatado
"""

from exercicio107 import moeda

# Programa Principal
valor = float(input('Digite o preço: R$'))
print(f'\033[94mA metade {moeda.moeda(valor)} \033[94mé {moeda.moeda(moeda.metade(valor))}')
print(f'\033[94mO dobro de {moeda.moeda(valor)} \033[94mé {moeda.moeda(moeda.dobro(valor))}')
print(f'\033[94mCom aumento de \033[96m10%\033[94m, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'\033[94mCom diminuição de \033[96m10%\033[94m, temos {moeda.moeda(moeda.diminuir(valor, 10))}')
