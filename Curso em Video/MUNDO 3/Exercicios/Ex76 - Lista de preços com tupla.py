listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Cadenero', 15.90,
            'Estojo', 25)

print('-'*39)
print(f'{"Listagem de Preços":^40}')
print('-'*39)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

print('-'*39)