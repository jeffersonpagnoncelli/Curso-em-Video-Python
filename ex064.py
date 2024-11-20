n = soma = contador = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma))


