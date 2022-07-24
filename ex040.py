"""
Crie um programa que leia duas notas
de um aluno e calcule a media,
mostrando uma mensagem no final,
de acordo com a media atingida:

- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO

"""
nome = str(input('Nome do aluno: '))
n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
média = (n1 + n2) / 2
print(f'Sua média é: {média}')
if média < 5:
    print(f'{nome}, você está <REPROVADO>')
elif média >= 7:
    print(f'{nome}, você está <APROVADO>')
else:
   print(f'{nome}, você está de <RECUPERAÇÃO>')