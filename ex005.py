"""
Crie um programa que leia um numero inteiro
                    e
mostre na tela seu antecessor e seu sucessor
"""

valor = int(input('\033[31mValor Inteiro: '))
suc = valor + 1
ant = valor - 1
print('\033[35mO valor {}, tem antecessor {} e sucessor {}'.format(valor, ant,suc))

"""
-----------------------------
  coreçao curso em video
-----------------------------
n = int(input('Digite um valor: '))
a = n - 1
s = n + 1
print('Analisando os valores {}, seu antecessor é {} e seu sucessor é {}'.format(n, a, s))

ou tambem 

n = int(input('Digite um valor: '))
print('Analisando os valores {}, seu antecessor é {} e seu sucessor é {}'.format(n, (n - 1), (n + 1)))
"""