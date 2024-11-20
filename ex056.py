soma_idades = 0
velho = []
idade_velho = 0
menor_idade = 0
for informacao in range(1, 5):
    print('---------- {}ª PESSOA ----------'.format(informacao))
    nome = str(input('Qual é seu nome?')).strip()
    idade = int(input('Qual é sua idade?'))
    sx = str(input('Masculino ou Feminino?')).strip()
    soma_idades += idade
    velho.append(sx)
    maior = max(velho)
    if sx.lower() == 'masculino' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sx.lower() == 'feminino' and idade < 20:
        menor_idade += 1


if idade_velho > 0:
    print(nome_velho)

media = soma_idades / 4
print('A média de idade do grupo é de {} anos, o nome do homem mais velho é {} com {} anos.'.format(media, nome_velho, idade_velho))
print('Temos {} mulheres com menos de 20 anos'.format(menor_idade))

