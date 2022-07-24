"""
Crie um programa onde o usuario digite uma EXPRESSÃO
qualquer que use PARENTESES. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses
abertos e fechados na ORDEM CORRETA
"""
expressão = input('Expressão matematica: ').strip()
parenteses = []
"""
if '(' in expressão:
    parenteses.append('(')
elif ')' in expressão:
    parenteses.append(')')
else:
    print('Sua expressão nao tem nenhum parenteses')
"""

"""
if expressão.count('(') == expressão.count(')'):
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')
"""

for item in expressão:
    if item == '(':
        parenteses.append('(')
    elif item == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

print()
#print('Lista: ', parenteses)
if len(parenteses) > 0:
    print('Expressão Incorreta')
elif len(parenteses) == 0:
    print('Expressão Correta')

