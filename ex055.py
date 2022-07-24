"""
Faça um programa que leia o PESO de CINCO PESSOA. No final,
mostre qual foi o MAIOR e MENOR peso lidos
"""
m_p = mn_p = 0
for pe in range(1, 5+1):
    peso = float(input(f'Peso {pe}° pessoa: '))
    if pe == 1:
        m_p = peso
        mn_p = peso
    else:
        if peso > m_p:
            m_p = peso
        if peso < mn_p:
            mn_p = peso

print(f'O maior peso lido foi {m_p}kg')
print(f'O menor peso lido foi {mn_p}kg')