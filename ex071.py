"""
Crie um programa que simule o funcionamento de um CAIXA ELETRONICO.
No inicio, pergunte ao usuario qual será o VALOR A SER SACADO(INT)
e o programa irá informar quantas CÉDULAS de cada valor serão entregues

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
print(' -'*11)
print('      Banco Max ')
print(' -'*11)


cedula = 50
total_cedulas = 0
valor_sacar = int(input('Qual valor deseja sacar: R$'))
final = valor_sacar
print()
print(f'Para sacar R${valor_sacar}')
while True:
    if final >= cedula:
        final -= cedula
        total_cedulas += 1

    else:
        if total_cedulas > 0:
            print(f'São necessarias um total de {total_cedulas} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if final == 0:
            break
print(' =-'*15)
print('Saque efetuado com sucesso')
