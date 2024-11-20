matriz = [[0, 0, 0], [0, 0, 0], [0, 0 ,0]]
segunda_linha = maior_valor = soma_par = soma_terceira_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_par = soma_par + matriz[l][c]
for linha in matriz:
    soma_terceira_coluna += linha[2]
segunda_linha = matriz[1]
maior_valor = max(segunda_linha)
print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor}')