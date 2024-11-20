valores = []
for pessoas in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    valores.append(peso)

maior = max(valores)
menor = min(valores)

print('O peso maior é de {}kg e o peso menor é de {}kg!'.format(maior, menor))

