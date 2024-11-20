import random

quantidade_numeros = 5
numeros_gerados =  tuple(random.randint(1, 10) for num in range(quantidade_numeros))
print(f'Os números gerados foram: ', end='')
for n in numeros_gerados:
    print(f'{n} ', end='')
maior = max(numeros_gerados)
menor = min(numeros_gerados)

print(f'\nO maior número é {maior} e o menor é {menor}!')