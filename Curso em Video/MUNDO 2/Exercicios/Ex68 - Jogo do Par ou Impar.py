import random

print('=' * 60)
print('Jogo - Par ou Impar'.center(60))
print('=' * 60)

contador = 0

while True:
    print('\n[P] - Par')
    print('[I] - Impar')

    par_impar = input('Digite a sua escolha: ').strip().upper()
    jogador = int(input('Digite um número de 0 a 10: '))

    computador = random.randint(0, 10)
    soma = computador + jogador

    print(f'\nVocê jogou {jogador} e o computador jogou {computador}. A soma é {soma}.')

    if par_impar == 'P':
        print('Você escolheu Par!')
        if soma % 2 == 0:
            print('A soma é PAR, você ganhou! Vamos para a próxima rodada!')
            contador += 1
        else:
            print(f'A soma é IMPAR, você perdeu! Você ganhou {contador} vez(es).')
            break
    elif par_impar == 'I':
        print('Você escolheu Impar!')
        if soma % 2 != 0:
            print('A soma é IMPAR, você ganhou! Vamos para a próxima rodada!')
            contador += 1
        else:
            print(f'A soma é PAR, você perdeu! Você ganhou {contador} vez(es).')
            break
    else:
        print('Opção inválida! Escolha [P] para Par ou [I] para Impar.')

print('\nFim do jogo! Obrigado por jogar!')