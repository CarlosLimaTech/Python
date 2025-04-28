print('=' * 60)
print('Progressão Aritimética'.center(60))
print('=' * 60)

termo = float(input('Digite o 1° termo: '))
razao = float(input('Agora digite a razão: '))

print('Os 10 primeiros termos da PA são:')

contador = 1
atual = termo

while contador <= 10:
    print(f'{atual:.2f}', end=' -> ')
    atual += razao
    contador += 1

print('FIM')