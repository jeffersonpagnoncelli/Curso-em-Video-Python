resultado = 1
contador = 1

fatorial = int(input('Digite um número para calcular o seu fatorial: '))
while contador <= fatorial:
    resultado *= contador
    print(resultado, end=" ")
    if contador < fatorial:
        print('*', end=" ")
    contador += 1

print('\nO fatorial de {} é {}'.format(fatorial, resultado))

"""from math import factorial
n = int(input('Digite um número para calcular o seu fatorial:))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f)
"""

#n = int(input('Digite um número para calcular o seu fatorial: '))
#c = n
#f = 1
#print('Calculando {}! = '.format(n), end='')
#while c > 0:
    #print({}.format(c), end='')
    #print(' x ' if c > 1 else ' = ', end='')
    #f *= c
    #c -= 1
#print('{}'.format(f))