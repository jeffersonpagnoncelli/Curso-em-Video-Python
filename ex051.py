primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for pa in range(primeiro, decimo + razao, razao):
    print('{}'.format(pa), end=' -> ')
print('Acabou!!')

#################################################
