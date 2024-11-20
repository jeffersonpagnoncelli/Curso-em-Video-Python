soma = 0
contador_mil = 0
barato = []
menor_preco = float('inf')


print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)

while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))

    if preco > 1000:
        contador_mil += 1

    if preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = produto
    soma += preco
    barato.append((produto, preco))


    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua == 'N':
        break

    if preco == menor_preco:
        nome_mais_barato = produto

    print('-'*40)

print('---------- FIM DO PROGRAMA ----------')

print(f'O total das compras deu R${soma}.00 reais.')
print(f'Temos {contador_mil} produtos custando mais de R$1000 reais.')
print(f'O produto mais barato foi o(a) {nome_mais_barato} que custa R${menor_preco}.00 reais.')
