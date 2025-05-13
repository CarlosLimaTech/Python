linha = list()
matriz = list()

for i in range(3):
    for j in range(3):
        linha.append(int(input(f'Digite o valor [{i}][{j}] - ')))
    
    matriz.append(linha[:])
    linha.clear()

print("\nMatriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()