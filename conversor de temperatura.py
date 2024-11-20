temperaturaC = contador = temperaturaF = 0

temperaturaC = int(input('Digite a temperatura em celsius para transformar em fahrenheit: '))
temperaturaF = (temperaturaC * 1.8) + 32
print('A temperatura em Fahrenheit é {} graus.'.format(temperaturaF))
continuar = str(input('Deseja continuar ? S/N: ')).strip().upper()

while continuar not in 'Nn':
    contador += 1
    temperaturaC = int(input('Digite a temperatura em celsius para transformar em fahrenheit: '))
    temperaturaF = (temperaturaC * 1.8) + 32
    print('A temperatura em Fahrenheit é {} graus.'.format(temperaturaF))
    continuar = str(input('Deseja continuar ? S/N: ')).strip().upper()
