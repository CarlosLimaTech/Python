print('='*40)
print(f'{"Maior e menor valores na lista":^40}')
print('='*40)

numeros = []
for indice in range(5):
    numero = int(input(f'Digite o {indice+1}° valor: '))
    numeros.append(numero)
print(f'Você digitou a lista - {numeros}\n')

print(f'O maior valor digitado foi o {max(numeros)} nas posições: ')
for contador, valor in enumerate(numeros):
    if valor == max(numeros):
        print(contador)

print(f'O menor valor digitado foi o {min(numeros)} nas posições: ')
for contador, valor in enumerate(numeros): 
    if valor == min(numeros):
        print(contador)