print('=' * 60)
print('Tratando Vários Valores'.center(60))
print('=' * 60)

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print('=' * 60)
print(f'Você digitou {contador} número(s) e a soma entre eles foi {soma}.')