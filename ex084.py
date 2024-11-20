pessoas = []
valores = []
cont = 0

while True:
    valores.append(str(input('Nome: ')))
    valores.append(float(input('Peso: ')))
    cont += 1
    continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    pessoas.append(valores[:])
    valores.clear()
    if continua in 'Nn':
        break

maior_peso = 0
pessoa_pesada = ''
menor_peso = float('inf')
pessoa_leve = ''
for pessoa in pessoas:
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
        pessoa_pesada = pessoa[0]
    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]
        pessoa_leve = pessoa[0]
pessoa_pesada = pessoa_pesada.capitalize()
pessoa_leve = pessoa_leve.capitalize()
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi {maior_peso}Kg do(a) {pessoa_pesada}. ')
print(f'O menor peso foi {menor_peso}Kg do(a) {pessoa_leve}.')
