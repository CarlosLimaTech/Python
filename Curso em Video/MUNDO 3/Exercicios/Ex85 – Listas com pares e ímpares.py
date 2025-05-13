numeros_pares = list()
numeros_impares = list()

for i in range(7):
    num = int(input(f'Digite o {i + 1}° número: '))

    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

numeros_pares.sort()
numeros_impares.sort()

print(f'\nLista com todos os números = {numeros_impares + numeros_pares}')
print(f'Lista com os números pares = {numeros_pares}')
print(f'Lista com os números ímpares = {numeros_impares}')