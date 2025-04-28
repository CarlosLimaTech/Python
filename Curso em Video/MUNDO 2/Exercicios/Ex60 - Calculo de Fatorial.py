print('=' * 60)
print('Cálculo de Fatorial'.center(60))
print('=' * 60)

numero = int(input('Digite um número para calcular seu fatorial: '))

fatorial = 1
contador = numero

print(f'\nCalculando {numero}! = ', end='')

while contador > 0:
    print('{contador}', end=' x ' if contador > 1 else ' = ')
    fatorial *= contador
    contador -= 1

print(f'{fatorial}')