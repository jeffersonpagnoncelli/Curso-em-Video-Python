lista = input('Digite uma lista de números separados por vírgula: ')

numeros = list(map(int, lista.split(', ')))

soma = sum(numeros)

print('A soma dos elementos é {} elementos.'.format(soma))