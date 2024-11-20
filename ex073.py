tabela = ('Bragantino', 'Flamengo', 'Botafogo', 'Athletico-PR', 'Gremio', 'Internacional', 'Atlético-MG', 'Fortaleza', 'Bahia', 'Fluminense', 'Palmeiras', 'Cruzeiro', 'Juventude', 'São Paulo', 'Vasco', 'Criciuma', 'Vitória', 'Corinthians', 'Atlético-GO', 'Cuiabá')

print(f'Os 5 primeiros colocados do Brasileirão 2024 são {tabela[0:5]}')
print(f'Os 4 últimos colocados do Brasileirão 2024 são {tabela[16:20]}')
ordem = sorted(tabela)
print(f'Os times em ordem alfabética são: {ordem}')
indice = tabela.index('Internacional') + 1
print(f'A posição do Internacional na tabela é a {indice}ª posição')