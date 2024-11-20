num = []
impar = []
par = []

while True:
    valores = int(input('Digite um número: '))
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if valores not in num:
        num.append(valores)
    if valores % 2 == 0:
        par.append(valores)
    if valores % 2 == 1:
        impar.append(valores)
    if continua != 'S':
        if continua == 'N':
            break
        else:
            print('Opção inválida! Tente novamente.')
            continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
