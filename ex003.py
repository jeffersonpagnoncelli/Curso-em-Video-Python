alt = float(input('Digite a altura da parede: '))
bas = float(input('Digite o comprimento da base da parede: '))
area = alt * bas
tinta = area / 2**2
print('O valor da area é {} e a quantidade de tinta necessaria para pintar essa area é de {}'.format(area, tinta))

preco = float(input('Digite o valor do preço do produto: '))
desconto = preco * 0.05
novo_preco = preco - desconto
print('O preço com 5% de desconto fica {}'.format(novo_preco))

salario = float(input('Digite o valor atual do seu salario: '))
aumento = salario * 0.15
novo_sal = salario + aumento
print('O seu salário com 15% de aumento é de {}'.format(novo_sal))