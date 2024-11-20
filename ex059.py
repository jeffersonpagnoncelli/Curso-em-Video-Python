
somar = 1
multiplicar = 2
maior = 3
novos_num = 4
sair = [5]
opcao = [1, 2, 3, 4, 5]
escolha = 0
novo_num1 = 0
novo_num2 = 0
p1 = float(input('Digite o primeiro valor: '))
p2 = float(input('Digite o segundo valor: '))
while escolha not in sair:

    print('   [ 1 ] somar \n   [ 2 ] multiplicar \n   [ 3 ] maior \n   [ 4 ] novos números \n   [ 5 ] sair do programa \n')
    escolha = int(input('>>>>>>>> Qual é sua opção? '))
    if escolha == 1:
        soma = p1 + p2
        resultado_soma = soma
        print('A soma dos números é {}.'.format(resultado_soma))


    elif escolha == 2:
        multiplicacao = p1 * p2
        resultado_multiplicacao = multiplicacao
        print('O resultado da multiplicação dos números é {}'.format(resultado_multiplicacao))

    elif escolha == 3:
        if p1 > p2:
            print('O número {} é maior que o {}.'.format(p1, p2))

        elif p2 > p1:
            print('O número {} é maior que o {}.'.format(p2, p1))


    elif escolha == 4:
        novo_num1 = float(input('Digite o primeiro novo número: '))
        novo_num2 = float(input('Digite o segundo novo número: '))

        subescolha = int(input(
            'Escolha a operação para os novos números:\n  [ 1 ] Somar\n  [ 2 ] Multiplicar\n  [ 3 ] Maior número\n >>>>>>>> Qual é sua opção? '))

        if subescolha == 1:
            resultado_soma = novo_num1 + novo_num2
            print('A soma dos novos números é {}.'.format(resultado_soma))

        elif subescolha == 2:
            resultado_multiplicacao = novo_num1 * novo_num2
            print('O resultado da multiplicação dos novos números é {}.'.format(resultado_multiplicacao))

        elif subescolha == 3:
            if novo_num1 > novo_num2:
                print('O número {} é maior que o {}.'.format(novo_num1, novo_num2))
            elif novo_num2 > novo_num1:
                print('O número {} é maior que o {}.'.format(novo_num2, novo_num1))

        else:
            print('Opção inválida para a operação com novos números. Tente novamente.')


    if escolha == 5:
        print('OBRIGADO POR USAR O PROGRAMA! FIM!')


    elif escolha not in opcao:
        print('Opção inválida! Tente novamente.')

