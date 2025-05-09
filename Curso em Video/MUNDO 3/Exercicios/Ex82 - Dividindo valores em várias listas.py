print('='*40)
print(f'{"Dividindo valores em várias listas":^40}')
print('='*40)

numeros = []
numeros_pares = []
numeros_impares = []

while True:
    num = int(input('Digite o valor: '))
    numeros.append(num)

    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    
    if continuar == 'N':
        break

print(f'Lista com todos os números = {numeros}\n')
print(f'Lista com os números pares = {numeros_pares}\n')
print(f'Lista com os números impáres = {numeros_impares}\n')