linha = list()
matriz = list()
soma_pares = soma_terceira_coluna = 0

for i in range(3):
    for j in range(3):
        linha.append(int(input(f'Digite o valor [{i}][{j}] - ')))

        if linha[j] % 2 == 0:
            soma_pares += linha[j]

        if j == 2:
            soma_terceira_coluna += linha[j]
    
    matriz.append(linha[:])
    linha.clear()

print("\nMatriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()

maior_segunda_linha = max(matriz[1])

print(f'\nA - Soma dos valores pares digitado = {soma_pares}')
print(f'\nB - Soma dos valores da 3° Coluna = {soma_terceira_coluna}')
print(f'\nC - O maior valor da 2° linha = {maior_segunda_linha}')