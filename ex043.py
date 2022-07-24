"""
Desenvolva uma logica  que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre,
de aordo com a tabela abaixo:
 -----------------------------------
|- Abaixo de 18.5: abaixo do peso   |
|- Entre 18.5 e 25: Peso ideal      |
|- 25 até 30: Sobrepeso             |
|- 30 até 40: Obesidade             |
|- Acima de 40: Obesidade morbida   |
 -----------------------------------
"""
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('SEU PESO ESTA IDEAL')
elif imc > 25 and imc < 30:
    print('VOCÊ ESTÁ COM SOBREPESO')
elif imc > 30 and imc < 40:
    print('CUIDADO!! VOCÊ ESTÁ COM OBESIDADE')
else:
    print('EXTREMO CUIDADO !!!!! VOCÊ ESTÁ COM OBESIDADE MORBIDA')
