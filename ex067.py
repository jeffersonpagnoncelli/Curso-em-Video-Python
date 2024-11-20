cont = 1
while True:
    print('-'*35)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        break
    for u in range(1,11):
        print(f'{n} x {u} = {n*u}')

print('TABUADA ENCERRADA. Volte sempre!')
