"""
Escreva um programa para aprovar um empréstimo bancario para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA,o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

calcule o valor da prestação mensal sabendo que ele não pode exceder 30% do salário
ou então o emprestimo será negado
"""
sal = float(input('Qual seu salário: R$ '))
valor_casa = float(input('Qual valor da casa: R$ '))
tempo = int(input('Em quantos anos deseja pagar: '))
prestaçao = valor_casa / (12 * tempo)
print(f'Para comprar uma casa de R${valor_casa:.2f} em {tempo} anos, você pagará R${prestaçao:.2f} por mês'.replace('.',','))
porcent_salario = sal * 30 / 100
if prestaçao > porcent_salario:
    print('Emprestimo Negado')
else:
    print('Emprestimo Aprovado')
