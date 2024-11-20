boletim = []
import time

while True:
    valores = []
    valores.append(str(input('Nome: ')))
    valores.append(float(input('Nota 1: ')))
    valores.append(float(input('Nota 2: ')))
    boletim.append(valores[:])

    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if continua in 'Nn':
        break
print(f"{'Nº':<3} {'Nome':<10} {'Média':>5}")
print('-'*25)

for idx, aluno in enumerate(boletim):
    nome = aluno[0].capitalize()
    notas = aluno[1:]
    media = sum(notas) / len(notas)

    print(f'{idx:<3} {nome:<10} {media:>5.1f}')
while True:
    mostra = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if mostra == 999:
        break
    if 0 <= mostra < len(boletim):
        aluno = boletim[mostra]

        print(f'Notas de {aluno[0].capitalize()} são {aluno[1]}, {aluno[2]}')
    else:
        print('Opção inválida! Tente novamente.')
print('FINALIZANDO...')
time.sleep(1)
print('<<< VOLTE SEMPRE >>>')