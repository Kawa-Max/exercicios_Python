"""
Escreva a programa que leia DOIS NUMEROS  e compare-os, mostrando na tela uma mensagem:

- O PRIMEIRO VALOR é MAIOR
- O SEGUNDO VALOR é MAIOR
- NÃO EXISTE valor maior, os dois são IGUAIS

"""
v_1 = int(input('Digite um valor: '))
v_2 = int(input('Outro valor: '))

if v_1 > v_2:
    print('O primeiro valor é \033[31mMAIOR\033[m')
elif v_2 > v_1:
    print('O segundo valor é \033[34mMAIOR\033[m')
elif v_1 == v_2:
    print('Não tem valor maior, os dois são \033[36mIGUAIS\033[m')