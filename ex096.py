def calcular_area(L, C):
    a = L * C
    print(f'A área de um terreno {L}x{C} é de {a:.1f}m²')


L = float(input('LARGURA (m): '))
C = float(input('COMPRIMENTO (m): '))
calcular_area(L, C)

