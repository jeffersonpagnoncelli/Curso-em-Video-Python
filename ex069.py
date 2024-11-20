contador_idade = 0
contador_sexo_homem = 0
contador_mulheres = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()

    if sexo == 'M':
        contador_sexo_homem += 1

    if idade >= 18:
        contador_idade += 1

    if sexo == 'F' and idade < 20:
        contador_mulheres += 1

    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if continua == 'N':
        break



print(f'Temos {contador_idade} pessoas com mais de 18 anos.')
print(f'Temos {contador_sexo_homem} homens cadastrados em nosso sistema.')
print(f'Temos {contador_mulheres} mulher(es) com menos de 20 anos em nosso sistema.')