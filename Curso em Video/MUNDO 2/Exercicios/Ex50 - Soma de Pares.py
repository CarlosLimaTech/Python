print('=' * 60)
print('Soma de Números Pares'.center(60))
print('=' * 60)

numeros = []

for i in range(0, 6):
    num = int(input(f'Digite o {i+1}º número: '))
    if num % 2 == 0:
        numeros.append(num)

soma = sum(numeros)

print('{}'.format(soma))