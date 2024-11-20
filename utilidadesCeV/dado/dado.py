def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.replace('.', '').isdigit() and entrada.count('.') <= 1:
            return float(entrada)
        else:
            print('\033[31mErro: valor inválido. Digite um valor monetário válido.\033[m')