def titulo(msg):
    tamanho_l = len(msg) + 4
    print('-' * tamanho_l)
    print(f'  {msg}')
    print('-' * tamanho_l)


# Modulo criado para execução dos exercicios 107, 108, 109, 110, 111 e 112

def metade(preco=0, form=False):
    resp = preco / 2
    if form:
        return moeda(resp)
    else:
        return resp


def diminuir(preco=0, porcentagem=10, form=False):
    resp = preco - (preco * porcentagem/100)
    if form:
        return moeda(resp)
    else:
        return resp


def aumentar(preco=0, porcentagem=10, form=False):
    resp = preco + (preco * porcentagem / 100)
    if form:
        return moeda(resp)
    else:
        return resp


def dobro(preco=0, form=False):
    resp = preco * 2
    if form:
        return moeda(resp)
    else:
        return resp


# Função Implementada no ex108
def moeda(preco=0, formatacao='R$'):
    return f'{formatacao}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, aum=10, dim=10):
    titulo('Resumo do valor')
    print('', '-' * 31)
    print(f'| Preço analisado: \t{moeda(preco)} \t|')
    print(f'| Dobro do preço: \t{dobro(preco, True)} \t|')
    print(f'| Metade do preço: \t{metade(preco, True)} \t|')
    print(f'| {aum}% de aumento: \t{aumentar(preco, aum, True)} \t|')
    print(f'| {dim}% de redução: \t{diminuir(preco, dim, True)} \t|')
    print('', '-' * 31)
