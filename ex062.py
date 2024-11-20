print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= razao:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('PAUSA')
while True:
    mais = int(input('\nDigite mais quantos números você deseja na sua PA: '))

    if mais == 0:
        break
    else:
        for i in range(mais):
            termo += razao
            print('{} -> '.format(termo), end='')
print('Fim da PA!')