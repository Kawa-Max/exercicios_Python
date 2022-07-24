"""
Escreva um programa que leia a velocidade de um carro

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado

A multa vai custar R$7,00 por cada km acima do limite
"""
vel = int(input('\033[34mQual velocidade atual do seu automovél ? '))
mult = (vel - 80) * 7
if vel > 80:
    print('\033[31mVocê foi multado em R${}, por ultrapassar o limite de velocidade(80 km/h)'.format(mult))
    print('\033[35mTenha mais calma e diminua a velocidade na proxima')
else:
    print('\033[32mContinue dirigindo em segurança')
print('\033[33mTenha um bom dia!!')
