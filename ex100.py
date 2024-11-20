import random
import time
valores = []

def sorteio():
    return random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
def somaPar(val):
    soma = 0
    for v in val:
        if v % 2 == 0:
            soma += v
    return soma


sorteados = sorteio()
print(f'Sorteando 5 valores da lista: ', end='')
for s in sorteados:
    time.sleep(0.5)
    print(s, end=' ',)
print('PRONTO!')
print()
valores.extend(sorteados)
resultado = somaPar(valores)
print(f'Somando os valores pares de {valores}, temos {resultado}')
