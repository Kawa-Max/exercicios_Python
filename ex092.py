"""
Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALAHO
e cadastre-os(com idade) em um DICIONARIO, se por acaso o CTPS for diferente de 0 ,
o dicionario receberá também o ANO DE CONTRATAÇÃO e o SALARIO. Calcule e
acrescente, além da IDADE, com quantos anos a pessoa vai se APOSENTAR
"""
from time import sleep
from _datetime import datetime


cidadao = dict()
cidadao['nome'] = str(input('Nome: ')).title().strip()
ano_nasc = int(input('Ano de Nascimento: '))
cidadao['idade'] = datetime.now().year - ano_nasc
cidadao['ctps'] = int(input('Carteira de Trabalho:(0 se não tem) '))
if cidadao['ctps'] > 0:
    cidadao['contratação'] = int(input('Ano de Contração: '))
    cidadao['salario'] = float(input('Salario: R$ '))
    cidadao['aposentadoria'] = cidadao['idade'] + ((cidadao['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in cidadao.items():
    print(f'{k:<15} ==> {v:>6}')
    sleep(0.5)
