"""
escreva um programa que leia um valor em metros
                e
o exiba convertido em cm e mm
"""
medida = int(input('\033[34mdigite um valor em metros: '))
cent = medida * 100
milin = medida * 1000
dm = medida * 10
kilometro = medida / 1000
pole = medida * 39.37
pe = medida * 3.281

print('\033[33mA media de {}m equivale a: \n{}cm;\n{}mm;'
      '\n{}dm\n{}km\n"{}\n+/-{}'
      .format(medida, cent, milin, dm, kilometro, pole, pe))
