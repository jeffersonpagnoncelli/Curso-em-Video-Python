import time

def texto():
    print('-='*30)
    print('Analisando os valores passados...')
def contador(*num):
    tam = len(num)
    if tam > 0:
        maior = max(num)
        for n in num:
            print(n, end=' ')
            time.sleep(1)
        print(f'Foram informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {maior}')
    else:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')




texto()
contador(2, 9, 4, 5, 7, 1)
texto()
contador(4, 7, 0)
texto()
contador(1, 2)
texto()
contador(6)
texto()
contador()
