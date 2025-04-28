print('=' * 60)
print('Progressão Aritimética'.center(60))
print('=' * 60)

termo = float(input('Digite o 1° termo: '))
razao = float(input('Agora digite a razão: '))

print('Os 10 primeiros termos da PA são:')
for i in range(10):  # Calcula os 10 primeiros termos
    print(f'{termo + i * razao:.2f}', end=' -> ')
print('FIM')