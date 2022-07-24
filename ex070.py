"""
Crie um programa que leia o NOME e PREÇO de VARIOS PRODUTOS.
O programa deverá perguntar ao usuario se irá continuar.No final,
mostre:

A) Qual é o TOTAL GASTO na compra

B) Quantos produtos custam MAIS de R$ 1000

C) Qual é o NOME do produto mais barato
"""
caro = barato = 0
tot_gasto = mais_1000 = c = 0
nome_barato = ''

print(' -'*10)
print('|  Mercadão do Max  |')
print(' -'*10)

while True:
    c += 1
    print('-'*15)
    produto = input('Nome do produto: ')
    preço = int(input('Preço: R$'))
    tot_gasto += preço

    if preço > 1000:
        mais_1000 += 1

    if c == 1:
        caro = barato = preço
        nome_barato = produto
    else:
        if preço > caro:
            caro = preço
        elif preço < caro:
            barato = preço
            nome_barato = produto

    resp = input('Continuar ?[S/N] ').upper()[0]
    while resp not in 'SsNn':
        print('Opção invalida, tente novamente...')
        resp = input('Continuar ?[S/N] ').upper()[0]
    if resp in 'nN':
        print('Analisando os produtos comprados')
        break
print()
print(f'O total gasto foi R${tot_gasto:.2f}')
print(f'Você comprou {mais_1000} produtos com preço acima de R$1.000,00')
print(f'O produto mais barato adquirido foi {nome_barato}, custando R${barato}')