from exercicios.ex115.usaveis import *


def arquivo_existente(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_Arquivo(arq):
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except:
        print('\033[91mOcorreu um erro ao tentar criar o arquivo\033[m')
    else:
        print(f'Arquivo {arq} criado com sucesso')


def verArquivo(arq):
    try:
        arquivo = open(arq, 'rt')
    except:
        print('\033[91mHouve um pequeno problema ao ler o arquivo \033[m')
    else:
        titulo('PESSOAS CADASTRADAS')

        print('', '\033[33m_\033[m' * 46, '')
        for pessoa in arquivo:
            dados = pessoa.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'| \033[94m{dados[0]:_<35}\033[96m{dados[1]:>4}\033[32m anos\033[m |')
            print(f'{"|":<47}|')
        print('|', '\033[33m_\033[m' * 44, '|')
    finally:
        arquivo.close()


def cadastro_novo(arq, n='<desconhecido>', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('\033[91mErro ao tentar abrir o arquivo\033[m')
    else:
        try:
            arquivo.write(f'{n};{idade}\n')
        except:
            print('\033[91mErro ao tentar escrever no arquivo\033[m')
        else:
            print(f'- \033[34m{n}\033[96m adicionado a lista\033[m')
            arquivo.close()


