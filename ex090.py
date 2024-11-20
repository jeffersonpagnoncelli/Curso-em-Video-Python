dados = {}
lista = []
for d in range(0, 1):
    dados['Nome'] = str(input('Nome: '))
    dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
    lista.append(dados.copy())
for i in lista:
    print(f'Nome é igual a {i["Nome"]}.\nMédia é igual a {i["Média"]}.')
    if dados['Média'] >= 7:
        print('Situação é igual a Aprovado.')
    else:
        print('Situação é igual a Reprovado')