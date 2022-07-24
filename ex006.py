"""
crie um algoritmo que leia um numero
            e
mostre o seu dobro, triplo e a raiz quadrada do valor

"""
"""
numeral = int(input('valor: '))
dobro = numeral * 2
triplo = numeral * 3
raiz= numeral ** (1/2)
print('O numeral {};\ntem dobro valendo {};\ntriplo valendo {} \ne raiz {}'.format(numeral, dobro, triplo, raiz))
"""
"""
----------------------------
coreçao curso em video

----------------------------
"""
n = int(input('\033[35mDigite um valor: '))
print('\033[31mO numero {},\ntem dobro {};\ntriplo {};\ne raiz quadrada {:.0f}\033[m'.format(n, (n*2), (n*3), pow(n, (1/2))))

