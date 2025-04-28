print('=' * 60)
print('Contagem de Pares'.center(60))
print('=' * 60)

print('Os úmeros pares no intervalo entre 1 e 50 são:')

for i in range(1, 51):
    if i % 2 == 0:
        print(i)