
def titulo(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

def ajuda(com):
    help(com)



comando = ''
while True:
    print("\033[48;30;42m", end="")
    titulo('SISTEMA de AJUDA PyHelp')
    print("\033[0m", end="")
    comando = str(input("Função ou Biblioteca > "))


    if comando.upper() == 'FIM':
        break
    else:
        print("\033[48;30;44m", end="")
        titulo(f'Acessando o manual do comando "{comando}".')
        print("\033[0m", end="")
        print("\033[48;5;255m\033[1;30m", end="")
        ajuda(comando)
        print("\033[0m", end="")


print("\033[48;30;41m", end="")
titulo('Até logo!')
print("\033[0m")





