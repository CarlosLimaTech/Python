print('='*40)
print(f'{"Lista ordenada sem repetições":^40}')
print('='*40)

numeros = []

for indice in range(5):
    numero = int(input(f'Digite o {indice+1}° valor: '))

    if len(numeros) == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista.')
    else:
        for pos in range(len(numeros)):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                print(f'Adicionado na posição {pos}.')
                break

print(f'\nVocê digitou a lista ordenada - {numeros}')