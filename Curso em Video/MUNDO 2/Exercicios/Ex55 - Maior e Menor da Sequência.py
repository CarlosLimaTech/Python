print('=' * 60)
print('Maior e Menor Peso'.center(60))
print('=' * 60)

maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa (em kg): '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'\nO maior peso registrado foi {maior_peso:.2f} kg.')
print(f'O menor peso registrado foi {menor_peso:.2f} kg.')