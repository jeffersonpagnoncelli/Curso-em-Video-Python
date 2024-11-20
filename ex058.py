from random import randint
import time
computador = randint(0, 10)
tentativas = 0

print('Sou seu computador...')
time.sleep(2)
print('Acabei de pensar em um número de 0 a 10')
time.sleep(1)
print('Será que você consegue adivinhar qual foi??')
time.sleep(2)

while True:
    num = int(input('Qual é seu palpite? '))
    tentativas += 1
    if num > computador:
        print('Menos...')
    elif num < computador:
        print('Maiss...')
    else:
        print('Você venceu! ')
        break
print('Você acertou em {} tentativas.'.format(tentativas))
print('FIM')








'''if num == computador:
    print('Você venceu!')

else:
    print('Você perdeu!')'''