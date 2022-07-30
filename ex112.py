"""
Dentro do pacote UTILIDADESCEV que criamos no ex111, temos um MÓDULO
chamado DADO. Crie um função chamada leiaDinheiro() que seja capaz de
funcionar como a função input(), mas com uma VALIDAÇÃO DE DADOS para
aceitar apenas valores que sejam MONETÁRIOS
"""
from utilidadesCeV import dado, moeda

money = dado.leiaDinheiro('R$')
moeda.resumo(money, 12, 5)
