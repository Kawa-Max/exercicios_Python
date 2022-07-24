"""
Desenvolva um programa que leia NOME, IDADE e SEXO de 4 PESSOAS. No final
do programa mostre:

- A MÉDIA DE IDADE do grupo;
- Qual é o nome do homem MAIS VELHO;
- Quantas mulheres tem MENOS DE 20 anos.
"""
soma = 0
idadev = 0
hvelho = ''
mulher20 = 0
for c in range(1, 4+1):
    print(f'======= {c}° PESSOA=======')
    nome = str(input('Nome ? ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    soma += idade
    if sexo in 'fF' and idade < 20:
        mulher20 += 1
    if c == 1 and sexo in 'Mm':
        hvelho = nome
        idadev = idade
    if sexo in 'mM':
        hvelho = nome
        idadev = idade

medía = soma / 4

print(f'A média de idade das pessoas cadastradas é: {medía}')
print(f'O homem mais velho é {hvelho}, com {idadev} anos')
print(f'Foram cadastradas, {mulher20} mulheres com menos de 20 anos')
