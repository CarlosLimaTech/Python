dado = list()
pessoas = list()
pesos = list()

while True:
    nome = str(input('\nDigite o nome da pessoa: '))
    peso = float(input('Digite o peso da pessoa: '))

    dado.append(nome)
    dado.append(peso)
    pessoas.append(dado[:]) 
    pesos.append(peso)
    
    dado.clear()

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'\nA - Foram cadastradas {len(pessoas)} pessoas.')

print(f'B - As pessoas mais pesadas ({maior_peso} kg) são: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')
print()

print(f'C - As pessoas mais leves ({menor_peso} kg) são: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')
print()