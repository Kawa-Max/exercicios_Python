from exercicios.ex115.usaveis import *
from exercicios.ex115.arquivos import *
from time import sleep

arquivo_txt = 'listapessoas.txt'

if not arquivo_existente(arquivo_txt):
    criar_Arquivo(arquivo_txt)


while True:
    limpaTela('cls')
    usuario = menu(['Novo cadastro: ', 'Ver pessoas cadastradas: ', 'Sair do Sistema'])
    if usuario == 1:
        titulo('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro_novo(arquivo_txt, nome, idade)
        sleep(1)

    elif usuario == 2:
        verArquivo(arquivo_txt)
        sleep(1)

    elif usuario == 3:
        print('Saindo do sistema, Até logo')
        pontos()
        sleep(1)

        break
    else:
        print('\033[91mErro! Digite uma opção válida!\033[m')
