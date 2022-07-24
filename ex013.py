"""
Faça um algoritmo que leia o salario de um funcionario
                e
mostre qual sera seu novo salario com 15% de aumento
"""
salario = float(input('\033[7;37mSalario atual: '))
aumento = salario + (salario * 15 / 100)
print('\033[1;31mCom 15% de aumento, o funcionario passará a receber R${:.2f}'.format(aumento))

