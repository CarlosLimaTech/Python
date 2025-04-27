import random

print('='*60)
print('Jogo da Advinhação'.center(60))
print('='*60)

numero_escolhido = int(input('Digite um número entre 0 e 5: '))
numero_sorteado = random.randint(0, 5)  # sorteia um número entre 0 e 5

print('Você escolheu o número {} e o computador escolheu o número {}'.format(numero_escolhido, numero_sorteado))

if numero_escolhido == numero_sorteado:
    print('Parabéns! Você acertou!')
else: 
    print('Você errou!')