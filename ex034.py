"""
Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento

Para salarios superiores a R$1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%
"""
sal = float(input('\033[34mQual salario do funcionario: '))

if sal >= 1250:
    aum = sal + (sal * 10 / 100)
else:
    aum = sal + (sal * 15 / 100)
print('\033[31mO funcionario que ganhava R${:.2f}, passa a ganhar {:.2f}'.format(sal, aum))
