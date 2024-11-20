n1 = 0
n2 = 1
print('►◄'*30)
print('Sequência de FIBONACCI')
print('►◄'*30)
sequencia = int(input('Digite o tamanho da sequência: '))
print('{} -> {} -> '.format(n1, n2), end='')
contador = 3

while contador <= sequencia:
    n3 = n1 + n2
    print('{} -> '.format(n3), end='')
    contador += 1
    n1 = n2
    n2 = n3
print('FIM')




