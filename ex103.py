def ficha(nome=None, gols=0):

    if nome == "":
        nome = None
    if nome is None:
        print(f'O jogador <desconhecido> fez {gols} gols(s) no campeonato. ')
    else:
        print(f'O jogador {nome} fez {gols} gols(s) no campeonato. ')
    return nome, gols


n = input('Digite o nome: ')
g = input('Número de gols: ')

if g == "":
    g = 0

else:
    g = int(g)

ficha(n, g)




