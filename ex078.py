"""
Crie um programa que leia 5 VALORES NUMERICOS e os guarde em uma LISTA.
No final, mostre qual foi o MAIOR e MENOR valor digitado e as suas
respectivas POSIÇÕES na lista
"""
"""maior = menor = 0
numeros = []

for num in range(0, 5):
    numeros.append(int(input(f'{num+1}° Posição: ')))
    if num == 0:
        maior = menor = numeros[num]
    else:
        if numeros[num] > maior:
            maior = numeros[num]
        elif numeros[num] < menor:
            menor = numeros[num]

print(f'Você digitou os valores {numeros}')

print(f"O maior valor foi '{maior}', na(s) posicão(ões) ", end='')
for indice_mai, valor_mai in enumerate(numeros):
    if valor_mai == maior:
        print(indice_mai+1, end='... ')

print()

print(f"O menor valor foi '{menor}', na(s) posicão(ões) ", end='')
for indice_men, valor_men in enumerate(numeros):
    if valor_men == menor:
        print(indice_men+1, end='.. ')

"""
lista_num = []
mai = 0
men = 0

for c in range(0, 5):
    lista_num.append(int(input(f'Digite um valor para a posição {c + 1}: ')))
    if c == 0:
        mai = men = lista_num[c]
    else:
        if lista_num[c] > mai:
            mai = lista_num[c]
        if lista_num[c] < men:
            men = lista_num[c]

print('=-' * 30)
print(f'Você digitou os valores {lista_num}')
print(f'O maior valor foi {mai}, nas posições ', end='')
for i, v in enumerate(lista_num):
    if v == mai:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor foi {men}, nas posições ', end='')
for i, v in enumerate(lista_num):
    if v == men:
        print(f'{i+1}...', end='')
print()
