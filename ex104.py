def obter_entrada_valida():
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            real = float(input("Digite um número real: "))
            return valor
        except ValueError:
            print("\033[1;31;48mEntrada inválida. Por favor, digite um número inteiro.\033[0m")


obter_entrada_valida()