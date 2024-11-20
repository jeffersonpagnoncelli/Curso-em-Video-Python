frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('É palindromo')

else:
    print('Não é palindromo')

########################################

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)

if inverso == junto:
    print('É palindromo')

else:
    print('Não é palindromo')'''

'''poderia ser usado dessa forma como fatiamento sem o uso do for'''