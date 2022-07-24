"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NUMERO ENTRE 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessarios para vencer
"""

from random import randint

palpite = 1
pc = randint(0, 10)
print('\033[31mSou seu computador\nPensei em um numero entre 0 e 10.')

ad = input('\033[36mConsegue adivinhar qual foi ?[S/N] ').strip().upper()[0]
while ad not in 'SsnN':
    ad = input('\033[31mErro na leitura. Digite apenas [S/N] ').strip().upper()[0]

if ad in 'Ss':
    opc = int(input('\033[35mQual numero pensei: '))
    while opc > 10:
        opc = int(input('\033[31mNúmero inválido\033[35mTente novamente: '))


    while pc != opc:
        if opc > pc:
            print()
            print('\033[36mMenos, tente novamente')
            opc = int(input('\033[34mQual seu palpite: '))
        elif opc < pc:
            print()
            print('\033[34mMais, tente novamente')
            opc = int(input('\033[36mQual seu palpite: '))
        palpite += 1
    print()
    print('\033[33mVocê acertou com {} palpites '.format(palpite))

else:
    print('\033[36mOk, talvez depois então):')

