from datetime import datetime
lista = []
dados = {}

for d in range(0, 1):
    dados['Nome'] = str(input('Nome: '))
    dados['Idade'] = int(input('Ano de nascimento: '))
    dados['Idade'] = datetime.now().year - dados['Idade']
    dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados['CTPS'] != 0:
        dados['Ano de Contratação'] = int(input('Ano de contratação: '))
        dados['Salário'] = float(input('Salário: '))
        dados['Aposentadoria'] = (dados['Ano de Contratação'] + 35) - (datetime.now().year - dados['Idade'])
    lista.append(dados.copy())
    if dados['CTPS'] == 0:
        break

for L in lista:
    for i, v in dados.items():
        if i == 'Salário':
            print(f'{i} tem o valor {v:.1f}')
        else:
            print(f'{i} tem o valor {v}')