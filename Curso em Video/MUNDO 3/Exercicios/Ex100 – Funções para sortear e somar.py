import random

numeros = list()

def sorteia():
    for i in range(5):
        numeros.append(random.randint(1, 100))

def somaPar(lista):
    soma_pares = 0
    for valor in lista:
        if valor % 2 == 0:
            soma_pares += valor
    print(f'A soma dos números pares é = {soma_pares}')

sorteia()
print(f'Os 5 números sorteados foram = {numeros}')
somaPar(numeros)