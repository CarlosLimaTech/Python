print('=' * 60)
print('É Número Primo?'.center(60))
print('=' * 60)

numero = int(input('Digite o número: '))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f'O número {numero} é PRIMO!')
else:
    print(f'O número {numero} NÃO é primo!')