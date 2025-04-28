print('=' * 60)
print('Maior, Menor e Média dos Valores'.center(60))
print('=' * 60)

soma = 0
contador = 0
maior = None
menor = None

while True:
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

media = soma / contador

print('=' * 60)
print(f'Você digitou {contador} número(s).')
print(f'A média dos valores é {media:.2f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')