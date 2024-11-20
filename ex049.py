n = int(input('Digite o número da tabuada que você deseja saber: '))
for c in range(0, 11):
    t = c * n
for j in range(0, 11):
    t = j * n
    print('{} x {} = {}'.format(j, n, t))

###################################OUUU FAÇA DESTE JEITO MAIS FACIL##########
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))



