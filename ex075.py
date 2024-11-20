valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o útlimo número: ')))
elemento = 3

print(f'Você digitou os valores {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if elemento in valores:
    print(f'A posição do primeiro número 3 é a {valores.index(3) + 1}ª posição.')
if elemento not in valores:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os números pares desta tupla são: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
