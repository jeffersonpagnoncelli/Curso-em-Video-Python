def mostralinha():
    print('-=' * 30)

mostralinha()
print('CALCULO DA CONTA DE ÁGUA'.center(50))
mostralinha()
taxabasica = float(input('Digite o valor da taxa básica: '))
mostralinha()
taxabasica = taxabasica / 4

preco_metro_agua = float(input('Digite o valor do metro da água: '))
mostralinha()
while True:
    metro_gasto = float(input('Digite o valor do metro de água gasto pelo morador: '))
    mostralinha()

    valor_para_somar = preco_metro_agua * metro_gasto
    valor_total = valor_para_somar + taxabasica

    print(f'O valor gasto pelo morador foi R${valor_total:.2f} reais.')

    continua = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if continua in 'Nn':
        print('<<FINALIZANDO>>'.center(50))
        break