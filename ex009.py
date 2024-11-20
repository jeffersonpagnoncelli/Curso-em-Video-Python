###########################################################################28:
from random import randint
computador = randint(0, 5)
num = int(input('Digite um número e tente descobrir qual número a maquina escolheu: '))
print('Pensei no número: {}'.format(computador))
if num == computador:
    print('Você venceu!')

else:
    print('Você perdeu!')

#########################################################################29:

vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    limite = vel - 80
    multa = limite * 7
    print('Você foi multado a {}km/h e o valor da multa é de {} reais'.format(vel, multa))
else:
    print('Você está dentro da velocidade permitida!')

#####################################################################30:
num = int(input('Digite um número para saber se é par ou impar: '))
if num % 2 == 0:
    print('É par!')

else:
    print('É ímpar!')

################################################################################31:
distancia_viagem = float(input('Digite a distância total da sua viagem: '))
if distancia_viagem <= 200:
    valor_passagem = distancia_viagem * 0.50
    print('O valor da sua passagem de {}km vai custar {}'.format(distancia_viagem, valor_passagem))
else:
    valor_passagem = distancia_viagem * 0.45
    print('O valor da sua passagem de {}km vai custar {}'.format(distancia_viagem, valor_passagem))

####################################################################################################32:
from datetime import date
bi = int(input('Digite qualquer ano para saber se é bissexto ou digite 0 para saber se o ano atual é bissexto: '))
if bi == 0:
    bi = date.today().year

if bi % 4 == 0 and bi % 100 != 0 or bi % 400 == 0:
    print('{} É bissexto!'.format(bi))

else:
    print('{} Não é bissexto!'.format(bi))

#########################################################################33:
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('O primeiro número escolhido foi {}, o segundo foi {} e o terceiro foi {}.'.format(n1,n2,n3))

lista = [n1,n2,n3]
mai = max(lista)
print('O maior número dessa lista é {}'.format(mai))

men = min(lista)
print('O menor número dessa lista é {}'.format(men))
#####################################################################################34:
salario = float(input('Digite o valor do seu salário para calcularmos o seu aumento: '))
if salario > 1250:
    aumento = salario * 0.1
    aumento = aumento + salario
    print('O seu salário atual é de {} e com o aumento passou para {}'.format(salario, aumento))

elif salario <= 1250:
    aumento = salario * 0.15
    aumento = aumento + salario
    print('O seu salario atual é de {} e com o aumento passou para {}'.format(salario, aumento))


