print('=' * 60)
print('Vários Números com Flag'.center(60))
print('=' * 60)

cont = numero = soma = 0

while True:
    numero = int(input('Digite um número: '))
    
    if numero == 999:
        break

    cont += 1
    soma = soma + numero

print(f'Você digitou {cont} números e a soma entre eles é {soma}')