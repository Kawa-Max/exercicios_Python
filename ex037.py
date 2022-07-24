"""
Escreva um programa que leia um numero inteiro qualquer e peça
ao usuario para escolher qual será a BASE DE CONVERSÃO

1 - para BINARIO
2 - para OCTAL
3 - para HEXADECIMAL

"""
n1 = int(input('Digite um numero inteiro: '))
conv = int(input('Qual será a base de conversão ?'
                 '\n1 - Binario'
                 '\n2 - Octal'
                 '\n3 - Hexadecimal'
                 '\n '
                 ))
if conv == 1:
    print(bin(n1)[2:])
elif conv == 2:
    print(oct(n1)[2:])
elif conv == 3:
    print(hex(n1)[2:])
else:
    print('Erro')
print('<<<FIM>>>')
