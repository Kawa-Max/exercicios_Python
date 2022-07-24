"""
faça um programa que leia uma frase qualquer pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- em que posiçao ela aparece a primeira vez
- em que posiçao ela aparece pela ultima vez
"""
frase = str(input('\033[31mDigite qualquer coisa: ')).upper().strip()
print("\033[33mA letra 'A' apareceu {} vezes".format(frase.count('A')))
print('e a sua primeira aparição é na posição {}'.format(frase.find('A') + 1))
print('e tambem, sua ultima aparição é na posição {}'.format(frase.rfind('A')))
# rfind(procure de traz pra frente e me mostre a posiçao)
