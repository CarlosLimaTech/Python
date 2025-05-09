print('='*40)
print(f'{"Valores únicos em uma lista":^40}')
print('='*40)

numeros = []

while True:
    num = int(input('Digite o valor desejado: '))

    if num not in numeros:
        numeros.append(num)
        print(f'{num} adicionado com sucesso!\n')
    else:
        print(f'{num} já está na lista, não vou adicionar....\n')

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    
    if continuar == 'N':
        break

numeros.sort()
print(f'\nOs valores digitados foram = {numeros}')