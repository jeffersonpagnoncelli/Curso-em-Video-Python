def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []

    with open(nome_arquivo, mode='r', encoding='utf8') as arquivo:
        for indice, linha in enumerate(arquivo, start=1):
            if indice == numero_linha:
                palavras_linha = linha.split()
                break

    return palavras_linha


linha = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=9)
print(linha)
