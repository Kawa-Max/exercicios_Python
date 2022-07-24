"""
Crie um programa que vai ler VARIOS NUMEROS e colocar em uma LISTA.

Depois disso, crie DUAS LISTAS EXTRAS que vão conter apenas os valores
PARES e os VALORES IMPARES digitados, respectivamente

Ao final, mostre o conteudo das 3 LISTAS geradas

"""
geral = []
pares = []
impares = []
c = 0
while True:
    c += 1
    valor = int(input(f'{c}° Valor: '))
    geral.append(valor)
    r = input('Quer continuar ? [S/N] ').upper()[0].strip()
    while r not in 'SN':
        r = input('\033[31mErro..\033[mQuer continuar ? [S/N] ').upper()[0].strip()

    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
    if r in 'N':
        break

print(f'Os valores digitados foram: {geral}')
print(f'Os valores pares são: {pares}')
print(f'E os valores impares são: {impares}')

