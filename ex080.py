"""
Crie um programa onde o usuario possa digitar cinco VALORES NUMERICOS
e cadastre-os em uma LISTA, JA NA POSIÇÃO CORRETA de inserção(sem usar o SORT()).

No final, mostre a LISTA ORDENADA na tela
"""
digitos = []
for c in range(0, 5):
    numero = int(input(f'{c+1}° valor: '))
    if c == 0 or numero > digitos[-1]:
        print('Adicionado a ultima posição da lista')
        digitos.append(numero)
    else:
        posição = 0
        while posição < len(digitos):
            if numero <= digitos[posição]:
                digitos.insert(posição, numero)
                print(f'Numero adicionado na {posição+1}° posição')
                break
            posição += 1
print('=-='*10)
print(f'E a list  a fica --> {digitos}')

