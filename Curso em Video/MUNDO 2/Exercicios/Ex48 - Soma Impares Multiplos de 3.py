print('=' * 60)
print('Contagem Rgressiva'.center(60))
print('=' * 60)

print('A soma dos número múltiplos de 3 e que são impares no intervalo entre 1 e 500 é:')

soma = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += 1

print('{}'.format(soma))