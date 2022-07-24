"""
Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado.
No final da execução, mostre a MÉDIA ENTRE TODOS os valores
e qual foi o MAIOR e o MENOR valor lido.
O programa deve perguntar ao usuario se ele quer ou nao CONTINUAR a digitar valores
"""
r = 'S'
c = s = mv = mnv = 0
while r == 'S':
    c += 1
    nm = int(input('{}° valor: '.format(c)))
    r = str(input('Deseja continuar:[S/N] ')).upper()[0]
    s += nm
    if c == 1:
        mv = mnv = nm
    else:
        if nm > mv:
            mv = nm
        if nm < mv:
            mnv = nm
media = s / c
print('A media dos valores digitados foi: {:.2f}'.format(media))
print('O maior valor foi {} e o menor foi {}'.format(mv, mnv))

