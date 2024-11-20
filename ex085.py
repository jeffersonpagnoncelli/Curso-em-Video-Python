numeros = [[], []]
valores = 0
for num in range(0, 7):
    valores = int(input('Digite o {}º valor: '.format(num + 1)))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)

numeros[0].sort()
numeros[1].sort()


print(f'Os valores pares digitados foram: {numeros[0]}.')
print(f'Os valores impares digitados foram: {numeros[1]}. ')



