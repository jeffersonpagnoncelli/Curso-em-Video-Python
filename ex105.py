def valores(*notas, sit=False):
    """

    :param notas: vários valores
    :return: valores adicionados dentro de um dicionario
    """
    maior = max(notas)
    menor = min(notas)
    total = len(notas)
    soma_notas = sum(notas)
    media = soma_notas / len(notas)
    dict = {}
    dict['Maior'] = maior
    dict['Menor'] = menor
    dict['Total'] = total
    dict['Media'] = media
    if sit:
        if dict['Media'] >= 7:
            dict['Situação'] = 'BOA'
        elif dict['Media'] >= 5:
            dict['Situação'] = 'RAZOÁVEL'
        else:
            dict['Situação'] = 'RUIM!'
    return dict


resp = valores(2.5, 10, 10, 6.5, sit=True)
print(resp)

