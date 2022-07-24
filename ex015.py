"""
faça um programa que  pergunte a quantidade de km percorrido
por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. CAucule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0.15 por km rodado
"""
km = int(input('\033[34mQual distancia percorrida (em km) : '))
dias = int(input('\033[31mQuantos dias o carro ficou alugado: '))
preco = (dias * 60 ) + (km * 0.15)
print('\033[4;35O preço a ser pago é R${:.2f}'.format(preco))
