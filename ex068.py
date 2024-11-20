from random import randint
cont = 0

while True:
    sorteio = randint(0, 10)
    valor = int(input('Diga um valor: '))
    resposta = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print('-'*40)

    soma = valor + sorteio
    if soma % 2 == 0 and resposta == 'P':
        print(f'Você jogou {valor} e o computador {sorteio}. Total de {soma} deu PAR')
        print('-' * 40)
        print('Você venceu!')
        cont += 1
    elif soma % 2 != 0 and resposta == 'I':
        print(f'Você jogou {valor} e o computador {sorteio}. Total de {soma} deu ÍMPAR')
        print('-' * 40)
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('-='* 20)
        cont += 1

    else:
        print(f'Você jogou {valor} e o computador {sorteio}. Total de {soma} deu {"PAR" if soma % 2 == 0 else "ÍMPAR"}')
        print('-' * 40)
        print('Você perdeu!')
        print('-=' * 20)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break

