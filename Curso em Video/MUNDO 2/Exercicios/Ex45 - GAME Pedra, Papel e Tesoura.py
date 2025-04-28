import random

print('=' * 60)
print('Pedra, Papel e Tesoura'.center(60))
print('=' * 60)

opcoes = ['Pedra', 'Papel', 'Tesoura']

print('Escolha sua jogada:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
jogador = int(input('Sua escolha: '))

if jogador < 0 or jogador > 2:
    print('Escolha inválida! Tente novamente.')
else:
    computador = random.randint(0, 2)

    print(f'\nVocê escolheu: {opcoes[jogador]}')
    print(f'O computador escolheu: {opcoes[computador]}')

    if jogador == computador:
        print('Empate!')
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print('Você venceu!')
    else:
        print('Você perdeu!')