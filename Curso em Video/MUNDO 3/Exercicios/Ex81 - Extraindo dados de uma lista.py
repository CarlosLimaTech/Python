print('='*40)
print(f'{"Extraindo dados de uma lista":^40}')
print('='*40)

numeros = []

while True:
    num = int(input('Digite o valor desejado: '))
    numeros.append(num)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    
    if continuar == 'N':
        break

numeros.sort(reverse=True)
print(f'\nA - Você digitou {len(numeros)} números!')
print(f'\nB - Os valores digitados foram = {numeros}')

if 5 in numeros:
    print('\nC - Sim, o número 5 faz parte da lista!')
else:
    print('\nC - Não, o número 5 não faz parte da lista!')