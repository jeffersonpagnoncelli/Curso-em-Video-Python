dados = {}
lista = []

while True:
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    lista_gols = []
    for p in range(partidas):
        gols = int(input(f'Quantos gols na partida {p}? '))
        lista_gols.append(gols)
    dados['Gols'] = lista_gols
    dados['Total'] = sum(lista_gols)
    lista.append(dados.copy())
    continua = str(input('Quer continuar? [S/N]: '))
    if continua in 'Nn':
        break


print(f"{'cod':<3} {'nome':<10} {'gols':<20} {'total':<5}")
print('-' * 40)
for i, jogador in enumerate(lista):
    gols_formatado = str(jogador['Gols']).replace('[', '').replace(']', '')
    print(f"{i:<3} {jogador['Nome']:<10} {gols_formatado:<20} {jogador['Total']:<5}")

while True:
    mostra = int(input('Mostrar dados de qual jogador? (Digite o código)(999 para parar) '))
    if mostra == 999:
        print('<< VOLTE SEMPRE >>')
        break
    if 0 <= mostra < len(lista):
        jogador = lista[mostra]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["Nome"]}')
        for i, gols in enumerate(jogador['Gols']):
            print(f'    No jogo {i + 1} fez {gols} gols.')

    else:
        print(f'ERRO! Não existe nenhum jogador com o código {mostra}! Tente novamente')




