num = []

while True:
    valor = int(input('Digite um valor: '))
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if valor not in num:
        num.append(valor)
    if continua != 'S':
        if continua == 'N':
            break
        else:
            print('Opção inválida! Tente novamente.')
            continua = str(input('Quer continuar? [S/N]: ')).strip().upper()

print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem descrescente são: {num}')
if 5 in num:
    print('O valor 5 está presente na lista.')
else:
    print('O valor 5 não está presente na lista.')