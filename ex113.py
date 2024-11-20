def obter_entrada_valida():
    real = 0.0
    valor = 0

    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("\033[1;31;48mEntrada inválida. Por favor, digite um número inteiro.\033[0m")
        except KeyboardInterrupt:
            print("\033[1;31;48mUsuário preferiu não digitar esse número.\033[0m")
            print(f'O valor inteiro digitado foi {valor} e o real foi {real}.')
            return

    while True:
        try:
            real = float(input('Digite um número real: '))
            break
        except ValueError:
            print("\033[1;31;48mEntrada inválida. Por favor, digite um número inteiro.\033[0m")
        except KeyboardInterrupt:
            print("\033[1;31;48mUsuário preferiu não digitar esse número.\033[0m")
            print(f'O valor inteiro digitado foi {valor} e o real foi {real}.')
        return

        print(f'O valor inteiro digitado foi {valor} e o real foi {real}.')

obter_entrada_valida()