
def voto(nasc=0):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - nasc
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')

    if 16 <= idade <= 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO. ')

    if idade >= 66:
        print(f'Com {idade} anos: VOTO OPCIONAL. ')

    return idade


nascimento = int(input('Em que ano você nasceu? '))
nascimento = voto(nascimento)

