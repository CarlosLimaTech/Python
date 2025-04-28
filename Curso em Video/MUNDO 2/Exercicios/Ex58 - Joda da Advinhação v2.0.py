import random

print('='*60)
print('Jogo da Advinhação 2.0'.center(60))
print('='*60)

numero_sorteado = random.randint(0, 10)
numero_escolhido = 20
contador = 0

while numero_sorteado != numero_escolhido:

    numero_escolhido = int(input('Digite um número entre 0 e 10: '))

    if numero_escolhido != numero_sorteado:
        print('Você errou! Tente novamente...')
        contador += 1

print('Parabéns, você acertou e precisou de {} vezes!'.format(contador))