listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*37)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-'*37)

print('{}'.format(listagem[0]),'.'*21,'R$','  {}'.format(listagem[1]))
print('{}'.format(listagem[2]),'.'*18,'R$','  {:.2f}'.format(listagem[3]))
print('{}'.format(listagem[4]),'.'*19,'R$',' {:.2f}'.format(listagem[5]))
print('{}'.format(listagem[6]),'.'*20,'R$',' {:.2f}'.format(listagem[7]))
print('{}'.format(listagem[8]),'.'*14,'R$','  {:.2f}'.format(listagem[9]))
print('{}'.format(listagem[10]),'.'*18,'R$','  {:.2f}'.format(listagem[11]))
print('{}'.format(listagem[12]),'.'*19,'R$','{:.2f}'.format(listagem[13]))
print('{}'.format(listagem[14]),'.'*19,'R$',' {:.2f}'.format(listagem[15]))
print('{}'.format(listagem[16]),'.'*21,'R$',' {:.2f}'.format(listagem[17]))
print('-'*37)
#metodo arrumado seria assim depois de colocar os valores na tupla:

#print('-' * 30)
#print('{"LISTAGEM DE PREÇOS":^40}')
#print('-' * 30)
#for pos in range(0, len(listagem)):
    #if pos % 2 == 0:
        #print(f'{listagem[pos]:.<30}', end='')
    #else:
        #print(f'R${listagem[pos]:>7.2f}')
#print('-' * 40)