"""
Crie um programa que leia VARIOS NÚMEROS inteiros pelo teclado. O programa só vai
parar quando o usuario digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final
mostre QUANTOS NUMEROS foram digitados e qual foi a SOMA entre eles(desconsiderando
o flag)
"""

n = soma = 0
quant = -1
while n != 999:
    quant += 1
    soma += n
    n = int(input('Digite um valor:(999 para parar) '))
    print('-'*5)

print('A soma dos valores digitados é: {}'
      '\n e a quantidade de numeros digitados foi {}'.format(soma, quant))
