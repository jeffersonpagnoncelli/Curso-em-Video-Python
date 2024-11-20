import random
import time

print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
quantidade = int(input('Quandos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantidade} JOGOS =-=-=-')

for sorteio in range(0, quantidade):
        numeros = random.sample(range(1, 61), 6)
        print(f'Jogo {sorteio + 1}: {numeros}')
        time.sleep(1)
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')
