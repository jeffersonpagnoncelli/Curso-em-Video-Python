num = []
while True:
    valor = int(input('Digite um valor: '))

    if valor in num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        num.append(valor)
        print('Valor adicionado com sucesso...')
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua != 'S':
        if continua == 'N':
            break
        else:
            print('Opção inválida! Tente novamente.')
            continua = str(input('Quer continuar? [S/N]: ')).strip().upper()

num.sort()
print('-='*30)
print(f'Você digitou os valores: {num}')
