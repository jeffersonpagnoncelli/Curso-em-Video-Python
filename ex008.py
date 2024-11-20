nome = 'Jefferson Pagnoncelli'
print(nome.upper())
print(nome.lower())
nome1 = nome.strip()
print(len(nome1))
nome = nome.split()
print(len(nome[0]))
##########################################################
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
###############################################################
nome = str(input('Digite o nome de uma pessoa: ')).strip()
print('O nome da pessoa é {}'.format(nome))
print('silva' in nome.lower())
###################################################
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[0:5].upper() == 'SANTO')

#####################################
algo = str(input('Digite qualquer palavra: ')).upper().strip()
print('A palavra que você escolheu é: {}'.format(algo))
print('O total de letras A dessa palavra é: {}'.format(algo.count('A')))
print('A primeira letra A aparece na posição: {}'.format(algo.find('A')+1))
print('A última letra A aparece na posição: {}'.format(algo.rfind('A')+1))
##########################################################################
nome = str(input('Digite o nome de uma pessoa: ')).strip()
print('O nome digitado é: {}'.format(nome))
nome = nome.split()
primeiro = nome[0]
ultimo = nome[-1]
print('O primeiro nome é {} e o ultimo nome é {}'.format(primeiro, ultimo))