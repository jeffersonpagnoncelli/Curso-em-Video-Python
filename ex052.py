limite = int(input('Digite até qual número você deseja classificar os números primos: '))

print('Números primos até {}:'.format(limite))

for num in range(2, limite+1):
    eh_primo = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(num, end=' ')


#################################

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo!')

else:
    print('E por isso ele não é primo!')
