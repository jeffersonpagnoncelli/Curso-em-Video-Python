dados = {}
lista_gols = []
lista = []

dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

for p in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {p}?'))
    lista_gols.append(gols)
dados['Gols'] = lista_gols
dados['Total'] = sum(lista_gols)
lista.append(dados.copy())
print('-='*30)
print(dados)
print('-='*30)
for l in lista:
    for c, v in l.items():
        print(f'O campo {c} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for j in range(0, partidas):
    print(f'    => Na partida {j}, fez {dados["Gols"][j]} gols.')
print(f'Foi um total de {dados["Total"]} gols')

