"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

- À vista DINHEIRO/CHEQUE: 10% de desconto
- À vista no CARTÃO: 5% DE DESCONTO
- Em até 2x NO CARTÃO: preço normal
- 3x OU MAIS no cartão: 20% de juros

"""
t = 'Mercadao do Max'
print(f'{t:_^30}')

preço = float(input('VALOR DO PRODUTO: R$'))
print('1 - DINHEIRO / CHEQUE(desconto 10%) '
      '\n2 - A VISTA no CARTÃO(desconto 5%) '
      '\n3 - 2x no CARTÃO(sem juros)'
      '\n4 - +3x no CARTÃO(20% de juros)'
      '\n5 - Cancelar compra'
      )
pagamento = int(input('Como deseja prosseguir: '))
if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'Com 10% de desconto, o produto custará R${desconto:.2f}'.replace('.', ','))
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print(f'Com 5% de desconto, o produto custará R${desconto:.2f}'.replace('.', ','))
elif pagamento == 3:
    parcela = preço / 2
    print(f'Dividido em duas vezes, paga-se R${parcela} cada parcela '.replace('.', ','))
elif pagamento == 4:
    par = int(input('Quantas parcelas? '))
    parc = (preço + (preço * 20 / 100)) / par
    print(f'em {par}x vezes, paga-se R${parc:.2f} por mês'.replace('.', ','))
elif pagamento == 5:
    print()
    print('Compra cancelada')
else:
    print('\033[31mOpção invalida\033[m')

