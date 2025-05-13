jogadores = list()

while True:
    jogador = dict()
    gols_por_jogo = list()

    jogador['Nome'] = str(input('Nome do Jogador: '))
    quantidade_jogos = int(input('Quantidade de Jogos: '))

    for i in range(quantidade_jogos):
        gols = int(input(f'Digite a quantidade de gols no {i + 1}° jogo: '))
        gols_por_jogo.append(gols)

    jogador['Gols'] = gols_por_jogo
    jogador['Total_Gols'] = sum(gols_por_jogo)

    jogadores.append(jogador.copy())

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print("\nResumo dos jogadores:")
print(f'{"Cod":<4}{"Nome":<15}{"Total de Gols":<15}')
print('-' * 40)
for indice, jogador in enumerate(jogadores):
    print(f'{indice:<4}{jogador["Nome"]:<15}{jogador["Total_Gols"]:<15}')

while True:
    opcao = int(input('\nMostrar dados de qual jogador? (999 para sair): '))
    if opcao == 999:
        print('Finalizando...')
        break
    if 0 <= opcao < len(jogadores):
        print(f'\nDetalhes do jogador {jogadores[opcao]["Nome"]}:')
        for i, gols in enumerate(jogadores[opcao]['Gols']):
            print(f'  No jogo {i + 1}, fez {gols} gols.')
    else:
        print('Opção inválida! Tente novamente.')