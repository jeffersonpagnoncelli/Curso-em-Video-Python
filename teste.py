credito = {'123': 750, '456': 812, '789': 980}

try:
    for chave, valor in credito.items():
        print(f'Para o documento {chave}, o valor do escore de crédito é {valor}.)
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}.')
else:
    print(f'Código executado sem erros.')