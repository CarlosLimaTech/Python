""" pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(f'Dado na posição pessoas [0][0] = {pessoas[0][0]}')
print(f'Dado na posição pessoas [1][1] = {pessoas[1][1]}')
print(f'Dado na posição pessoas [2][0] = {pessoas[2][0]}')
print(f'Dado na posição pessoas [1] = {pessoas[1]}') """

teste = list()
galera = list()

teste.append('Gustavo')
teste.append(40)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)