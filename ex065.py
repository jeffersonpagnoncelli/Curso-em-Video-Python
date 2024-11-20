soma = contador = 0
resposta = 'S'
numeros = []
while resposta == 'S':
    n = int(input('Digite um número: '))
    numeros.append(n)
    contador += 1
    soma += n
    resposta = input('Quer continuar? [S/N]').strip().upper()

media = soma / contador
maior = max(numeros)
menor = min(numeros)

print('Você digitou {} números e a média entre eles foi de {}.'.format(contador, media))
print('O maior número é {} e o menor número é {}.'.format(maior, menor))





