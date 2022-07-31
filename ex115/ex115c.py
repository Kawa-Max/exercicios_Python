from usaveis import *
from arquivos import *
from time import sleep


arquivo_txt = 'listapessoas.txt'

if not arquivo_existente(arquivo_txt):
    criar_Arquivo(arquivo_txt)

while True:
    limpaTela('cls')
    usuario = menu(['Novo cadastro ', 'Ver pessoas cadastradas ', 'Sair do Sistema'])
    if usuario == 1:
        titulo('Novo Cadastro')
        nome = str(input('\033[36mNome: \033[m')).title().strip()
        idade = leiaInt('\033[31mIdade: \033[m')
        cadastro_novo(arquivo_txt, nome, idade)

    elif usuario == 2:
        verArquivo(arquivo_txt)

    elif usuario == 3:
        print('\033[30mSaindo do sistema, Até logo', end='')
        pontos()
        break

    else:
        print('\033[91mErro! Digite uma opção válida!\033[m')
    sleep(1)

