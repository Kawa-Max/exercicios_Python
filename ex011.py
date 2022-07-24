"""
faça um programa que leia a largura e a altura de uma parede em metros,
calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo
que cad litro de tinta pinta uma area de 2m².

"""
alt = float(input('\033[43mAltura da parede em metros: '))
larg = float(input('Largura da parede em metros: \033[m'))
area = larg * alt
print('\033[36mCom dimensao {}x{}, a parede tem area {}m²'.format(alt, larg, area))
tinta = area / 2
print('\033[35mPara pintar sua parede, será nescessario {}L de tinta'.format(tinta))