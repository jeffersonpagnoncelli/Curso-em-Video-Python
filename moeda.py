def aumentar(num, valor=0, formatar=False):
    valor = valor / 100
    aumenta_valor = num + (num * valor)
    if formatar:
        return moeda(aumenta_valor)
    else:
        return aumenta_valor


def diminuir(num, valor=0, formatar=False):
    valor = valor / 100
    diminui_valor = num - (num * valor)
    if formatar:
        return moeda(diminui_valor)
    else:
        return diminui_valor


def dobro(num, formatar=False):
    dobro_valor = num * 2
    if formatar:
        return moeda(dobro_valor)
    else:
        return dobro_valor


def metade(num, formatar=False):
    metade_valor = num / 2
    if formatar:
        return moeda(metade_valor)
    else:
        return metade_valor


def moeda(num):
    return (f'R$ {num:.2f}'.replace('.', ','))


def resumo(preco, porcentagem1, porcentagem2):
    print('-' * 50)
    print(f'{"RESUMO DO VALOR".center(50)}')
    print('-' * 50)
    print(f'Preço analisado:    {moeda(preco)}')
    print(f'Dobro do preço:     {dobro(preco, True)}')
    print(f'Metade do preço:    {metade(preco, True)}')
    print(f'80% de aumento:     {aumentar(preco, porcentagem1, True)}')
    print(f'35% de redução:     {diminuir(preco, porcentagem2, True)}')
    print('-' * 50)


