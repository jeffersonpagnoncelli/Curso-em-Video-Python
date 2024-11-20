#nome = str(input('Digite o seu nome: '))
#if nome == 'Jefferson':
    #print('Que nome bonito!')

#elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
   #print('O seu nome é bem popular no Brasil.')
#elif nome in 'Ana Joana Alana Betania':
    #print('Belo nome feminino.')

#else:
    #print('Seu nome é bem normal!')

#print('Tenha um ótimo dia {}!'.format(nome))
#------------------------------------------------------------------------------------------------------#
emprestimo = float(input('Digite o valor do emprestimo que você deseja comprar: '))
salario = float(input('Digite o valor do seu salário atualmente: '))
anos = int(input('Digite em quantos anos você deseja pagar esta casa: '))
convertendo = anos * 12

prestacao = emprestimo / convertendo
salario_excedeu = salario * 0.3

if prestacao > salario_excedeu:
    print('O empréstimo será negado pois ultrapassa 30% do seu salário')

else:
    print('O empréstimo foi aprovado e você irá pagar {:.2f} reais mensais, durante {:.2f} anos sob juros 0.'.format(prestacao, anos))

print('##################################################################################')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número é maior!')

elif num2 > num1:
    print('O segundo número é maior! ')

else:
    print('Os números são iguais! ')

print('##################################################################################')

from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - nascimento
print('Sua idade é {} anos.'.format(idade))

if idade < 18:
    quanto_falta = 18 - idade
    print('Não está na hora ainda de você se alistar, faltam {} anos pra você se alistar!'.format(quanto_falta))

elif idade == 18:
    print('Está na hora de você se alistar!')

elif idade > 18:
    passou_quanto = idade - 18
    print('Já passou {} anos do prazo de alistamento militar, aliste-se já! '.format(passou_quanto))
print('##################################################################################')

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você está reprovado! ')

elif media >= 5.0 and media <= 6.9:
    print('Você está de recuperação, precisa estudar mais! ')

else:
    print('Você está aprovado! ')

print('##################################################################################')

from datetime import date
quando_nasceu = int(input('Digite o ano em que você nasceu: '))
a_idade = date.today().year - quando_nasceu
print('Você tem {} anos de idade, vamos ver em qual categoria você se encaixa.'.format(a_idade))

if a_idade <= 9:
    print('Você se encaixa na categoria: MIRIM!')

elif a_idade > 9 and a_idade <= 14:
    print('Você se encaixa na categoria: INFANTIL!')

elif a_idade > 14 and a_idade <= 19:
    print('Você se encaixa na categoria: JUNIOR!')

elif a_idade > 19 and a_idade <= 25:
    print('Você se encaixa na categoria: SÊNIOR!')

else:
    print('Você se encaixa na categoria: MASTER!')

print('##################################################################################')

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso!')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal! ')

elif imc >= 25 and imc <=30:
    print('Você está com sobrepeso!')

elif imc >= 30 and imc <= 40:
    print('Você está com obesidade!')

else:
    print('Você está com obesidade mórbida!')

print('##################################################################################')

import random

jokenpo = str(input('Escolha o que você vai jogar no pedra, papel ou tesoura: '))
lista = ['pedra', 'papel', 'tesoura']
maquina = random.choice(lista)

if jokenpo == maquina:
    print('Ninguém ganhou, jogue novamente!')

elif jokenpo == 'pedra' and maquina == 'tesoura':
    print('Você venceu, a máquina escolheu {}'.format(maquina))

elif jokenpo == 'pedra' and maquina == 'papel':
    print('Você perdeu, a máquina escolheu {}'.format(maquina))

elif jokenpo == 'papel' and maquina == 'tesoura':
    print('Você perdeu, a máquina escolheu {}'.format(maquina))

elif jokenpo == 'papel' and maquina == 'pedra':
    print('Você venceu, a máquina escolheu {}'.format(maquina))

elif jokenpo == 'tesoura' and maquina == 'pedra':
    print('Você perdeu, a máquina escolheu {}'.format(maquina))

elif jokenpo == 'tesoura' and maquina == 'papel':
    print('Você venceu, a máquina escolheu {}'.format(maquina))

print('##################################################################################')

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Opção inválida. Tente novamente.')

print('##################################################################################')

print('{:=^40}'.format(' LOJAS HAVAN '))
preco = float(input('Preço total das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] 2x no cartão: preço normal
[ 4 ] 3x ou mais com 20% de juros''')
opçao = int(input('Qual é a opção?'))

if opçao == 1:
    total = preco - (preco * 0.1)

elif opçao == 2:
    total = preco - (preco * 0.05)

elif opçao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))

elif opçao == 4:
    total = preco + (preco * 0.2)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas, parcela))

else:
    total == 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))




