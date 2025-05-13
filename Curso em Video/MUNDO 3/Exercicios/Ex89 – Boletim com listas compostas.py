boletim = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print(f'\n{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    opcao = int(input('\nMostrar notas de qual aluno? (999 para interromper): '))
    if opcao == 999:
        print('Finalizando...')
        break
    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}')
    else:
        print('Opção inválida! Tente novamente.')