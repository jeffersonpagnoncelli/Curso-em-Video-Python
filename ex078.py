valor = []

valor = (int(input('Digite um valor para a posição 0: ')),
         int(input('Digite um valor para a posição 1: ')),
         int(input('Digite um valor para a posição 2: ')),
         int(input('Digite um valor para a posição 3: ')),
         int(input('Digite um valor para a posição 4: ')),
         int(input('Digite um valor para a posição 5: ')))
print('=-'*30)
print(f'Você digitou os valores: {valor}')
maiorvalor = max(valor)
menorvalor = min(valor)

posicaomaior = [c for c, v in enumerate(valor) if v == maiorvalor]
posicaomenor = [c for c, v in enumerate(valor) if v == menorvalor]

print(f'O maior valor digitado foi {maiorvalor} nas posições {posicaomaior}...')
print(f'O menor valor digitado foi {menorvalor} nas posições {posicaomenor}... ')


