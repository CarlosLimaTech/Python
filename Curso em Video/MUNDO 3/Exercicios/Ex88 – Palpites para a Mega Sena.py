import random
from time import sleep

quantidade_jogos = int(input('Quantos jogos quer gerar? '))
print('')
jogo = list()
lista_jogos = list()

for indice in range(quantidade_jogos):
    for contador in range(6):
        jogo.append(random.randint(1, 60))
    
    lista_jogos.append(jogo[:])
    jogo.clear()

for contador, lista in enumerate(lista_jogos):
    print(f'{contador + 1}° jogo = {lista}')
    sleep(1)
    