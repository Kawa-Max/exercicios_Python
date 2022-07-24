"""
Crie um programa que tenha uma FUNÇÃO chamada voto() que vai receber como
PARAMETRO o ANO DE NASCIMENTO de uma pessoa, RETORNANDO um valor LITERAL
indicando se a pessoa tem voto NEGADO, OPCIONAL, ou OBRIGÁTORIO nas eleições
"""


def voto(ano):
    import datetime
    idade = datetime.datetime.now().year - ano
    if idade < 18:
        return f'\033[96m{idade} \033[94manos: Voto \033[91mNegado'
    elif idade >= 65:
        return f'\033[96m{idade} \033[94manos Voto \033[95mOpcional'
    else:
        return f'\033[96m{idade} \033[94manos: Voto \033[92mObrigátorio'


nasci = int(input('Ano de nascimento: '))
print(voto(nasci))
