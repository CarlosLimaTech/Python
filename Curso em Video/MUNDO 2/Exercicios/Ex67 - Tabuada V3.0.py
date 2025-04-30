print('=' * 60)
print('Tabuada V3.0'.center(60))
print('=' * 60)

numero = 0
indice = 0

while True:
    numero = int(input('Digite o número para visualizar a tabuada: '))

    if numero < 0:
        break
    
    print('=' * 20)
    print(f'Tabuada do {numero}\n')

    for indice in range (1, 11):
        print(f'{numero:2} X {indice:2} = {numero * indice:2}')

    print('=' * 20)

    indice = 0

print(f'Parece que você digitou um número negativo e por isso p programa foi interrompido... {numero}')            