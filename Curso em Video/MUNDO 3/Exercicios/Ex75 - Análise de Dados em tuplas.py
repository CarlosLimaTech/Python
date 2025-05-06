valores = ()

for i in range(4):
    valor = int(input(f'Digite o {i+1}° valor: '))
    valores += (valor,)

print(f'\nOs valores digitados foram: {valores}')

if 9 in valores:
    print(f'\nA - O número 9 aparece {valores.count(9)} veze(s)')
else:
    print('\nO número 9 não está na tupla!')

if 3 in valores:
    print(f'\nB - O primeiro número 3 aparece na posição {valores.index(3)} que é equivalente ao {valores.index(3) + 1}° número digitado')
else:
    print('\nO número 3 não está na tupla')

pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

print(f'\nC - Os números pares digitados foram: {pares}')