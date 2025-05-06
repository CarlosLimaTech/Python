import random

#forma facil de fazer
print("Forma número 1:")
numeros = tuple(random.sample(range(1, 100), 5))
print(f'Números sorteados: {numeros}')

maior = max(numeros)
menor = min(numeros)

print(f'O maior número é o {maior} e o menor é o {menor}\n')

#forma raiz de fazer
print("Forma número 2:")

numeros = tuple(random.sample(range(1, 100), 5))
print(f'Números sorteados: {numeros}')

menor = maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f'O maior número é o {maior} e o menor é o {menor}')