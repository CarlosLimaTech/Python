print('='*60)
print('Maior e Menor'.center(60))
print('='*60)

numeros = [
    float(input('Digite o 1° número: ')),
    float(input('Digite o 2° número: ')),
    float(input('Digite o 3° número: '))
]

print('O maior número é o {}'.format(max(numeros)))
print('O menor número é o {}'.format(min(numeros)))