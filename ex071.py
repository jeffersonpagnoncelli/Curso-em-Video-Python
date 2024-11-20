div50 = 0
div20 = 0
div10 = 0
div1 = 0
print('='*50)
print('{:^45}'.format('BANCO'))
print('='*50)

while True:
    valor = int(input('Que valor você quer sacar? R$ '))

    if valor > 0:
        div50 = valor // 50
        valor = valor - (div50 * 50)

        div20 = valor // 20
        valor = valor - (div20 * 20)

        div10 = valor // 10
        valor = valor - (div10 * 10)

        div1 = valor
    if div50 > 0:
        print(f'Total de {div50} células de R$50')
    if div20 > 0:
        print(f'Total de {div20} células de R$20')
    if div10 > 0:
        print(f'Total de {div10} células de R$10')
    if div1 > 0:
        print(f'Total de {div1} células de R$1')
    break
print('='*50)
print('Volte sempre ao BANCO! Tenha um bom dia!')

