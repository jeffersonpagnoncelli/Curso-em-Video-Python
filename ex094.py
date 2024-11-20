dados = {}
lista = []
mulheres = []
soma_idade = 0
acima_media = []

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    dados['Idade'] = int(input('Idade: '))

    soma_idade += dados['Idade']
    lista.append(dados.copy())

    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])

    continua = str(input('Quer continuar? [S/N]: '))
    if continua in 'Nn':
        break

cont = len(lista)
media = soma_idade / cont

for pessoa in lista:
    if pessoa['Idade'] > media:
        acima_media.append(pessoa)

print('-=' * 30)
print(f'O grupo tem {cont} pessoas.')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: {", ".join(mulheres)}')

if acima_media:
    print('Pessoas com idade acima da média: ')
    for pessoa in acima_media:
        print(f'Nome: {pessoa["Nome"]}, Sexo: {pessoa["Sexo"]}, Idade: {pessoa["Idade"]}')
else:
    print('Nenhuma pessoa tem idade acima da média.')

print('<< ENCERRADO >>')
