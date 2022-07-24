"""
Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS E SEUS
RESPECTIVOS PREÇOS, na sequencia

No final, mostre uma listagem de preços, organizando os dados de forma TABULAR
"""

print('_'* 40)
print(f'|{"Lista de produtos e Preços":^39}|')
print('_'* 40)


mercadoria_preço = ('Lapis',
                    3.5,
                    'Caderno',
                    17.9,
                    'Notebook',
                    2390.90,
                    'Smartphone',
                    1344.99,
                    'Geladeira',
                    987.50,
                    'Suporte para vidro',
                    25.90,
                    'Copo',
                    7.80,
                    'Mouse',
                    20,
                    'Mouse Pad',
                    14.50
                    )
for produto in range(0, len(mercadoria_preço)):
    if produto % 2 == 0:
        print(f'|\033[33m{mercadoria_preço[produto]:.<27} ', end='')
    else:
        print(f'\033[32mR$\033[31m{mercadoria_preço[produto]:>8.2f} \033[m|')
print('_'* 40)
