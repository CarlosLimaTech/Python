from random import randint
from operator import itemgetter

lista_jogador = []

for i in range(4):
    jogada = {
        'Nome': f'Jogador {i + 1}',
        'Valor': randint(1, 6)  # Valor aleatório entre 1 e 6
    }
    lista_jogador.append(jogada)

print("\nResultados:")
for jogador in lista_jogador:
    print(f"{jogador['Nome']} tirou {jogador['Valor']} no dado.")

lista_jogador.sort(key=itemgetter('Valor'), reverse=True)

print("\nRanking dos jogadores:")
for posicao, jogador in enumerate(lista_jogador, start=1):
    print(f"{posicao}º lugar: {jogador['Nome']} com {jogador['Valor']}")