"""
Desenvolva um programa que leia SEIS VALORES INTEIROS e mostre a soma de
apenas aqueles que forem PARES. Se o valor digitado for IMPAR, desconsidere-o
"""
s = 0
for c in range(1, 6+1):
    num = int(input(f'{c}° valor: '))
    if num % 2 == 0:
        s += num

print(f'Dentre os valores digitados, a soma entre os numeros pares é: {s}')


