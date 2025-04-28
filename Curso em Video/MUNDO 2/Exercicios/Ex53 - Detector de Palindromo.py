print('=' * 60)
print('Detector de Palíndromo'.center(60))
print('=' * 60)

frase = input('Digite uma frase: ').strip().lower()

frase_sem_espacos = frase.replace(' ', '')

if frase_sem_espacos == frase_sem_espacos[::-1]:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um palíndromo!')