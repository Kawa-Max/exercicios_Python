"""
Crie um programa que leia IDADE e o SEXO de VARIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá perguntar se o
USUARIO quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 ANOS

B) quantos HOMENS foram cadastrados

C) quantas MULHERES tem menos de 20 ANOS
"""

print('     Sistema de Cadastro')


p = maior_18 = homens_c = mulher_20 = 0
while True:
    p += 1
    print('-='*10)
    print(f'     {p}° PESSOA')
    print('-='*10)
    idade = int(input('Idade: '))
    while idade < 1 or idade > 80:
        if idade < 1:
            print('Apenas pessoas acima de 1 ano podem ser cadastradas')
            idade = int(input('Idade: '))
        elif idade > 80:
            print('Apenas pessoas abaixo de 80 anos podem ser cadastradas')
            idade = int(input('Idade: '))
    maior_18 += 1
    sexo = input('Sexo:[M/F] ').upper()[0]
    while sexo not in 'MmFf':
        print('\033[31mSexo invalido, tente novamente..')
        sexo = input('Sexo:[M/F] \033[m').upper()[0]
    if sexo in 'mM':
        homens_c += 1
    elif sexo in 'fF' and idade < 20:
        mulher_20 += 1
    continuar = input('Continuar ?[S/N] ').upper()[0]
    while continuar not in 'SsNn':
        print('\033[31mResposta errada, tente novamente..')
        continuar = input('Continuar ?[S/N] \033[m').upper()[0]
    if continuar == 'N':
        print('Analisando os dados digitados')
        break
print()
print(f'Foram cadastradas, {maior_18} pessoas acima de 18 anos')
print(f'{homens_c} homens cadastrados')
print(f'E um total de {mulher_20} mulheres menores de 20 anos')

print('<<<Fim>>>')
