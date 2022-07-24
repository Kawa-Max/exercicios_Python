"""
Faça um programa que leia NOME E MÉDIA de um aluno, guardando também a
SITUAÇÃO em um dicionario. No final, mostre o contéudo da estrutura na tela
"""

estudante = dict()
estudante['nome'] = str(input('\033[94mNome: ')).title().strip()
estudante['media'] = float(input(f'\033[96mMédia de \033[94m{estudante["nome"]}\033[96m: '))
if estudante['media'] >= 7:
    estudante['situação'] = '\033[32mAprovado'
elif 5 <= estudante['media'] < 7:
    estudante['situação'] = '\033[33mRecuperação'
else:
    estudante['situação'] = '\033[91mREPROVADO'

print()
for k, v in estudante.items():
    print(f'\033[93m{k}\033[31m tem valor \033[33m{v}')
