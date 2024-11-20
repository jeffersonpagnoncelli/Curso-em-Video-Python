cont = s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos números é {s} e foram digitados {cont} valores!')