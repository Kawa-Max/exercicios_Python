"""
desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens de ate 200 km
e R$0.45 para viagens mais longas
"""
dist = int(input('\033[45mQual distancia da sua viagem(em km): \033[m'))

if dist <= 200:
    passagem = dist * 0.5
    print('\033[32mO valor da passagem será de : {}'.format(passagem))
else:
    passagem = dist * 0.45
    print('\033[36mO valor da passagem para {}km é de : {}'.format(dist, passagem))

