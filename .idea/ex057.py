genero = str(input('Digite o seu gênero [M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('ERRO! Por favor, digite novamente usando M ou F: ')).strip().upper()[0]

if genero == 'M':
    print('O seu gênero é masculino, obrigado pela informação!')
else:
    print('O seu gênero é feminino, obrigado pela informação!')