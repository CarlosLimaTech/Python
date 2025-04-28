print('=' * 60)
print('Progressão Aritimética'.center(60))
print('=' * 60)

termo = float(input('Digite o 1° termo: '))
razao = float(input('Agora digite a razão: '))

contador = 1
atual = termo
total_termos = 10
mais_termos = 10

print('Os termos da PA são:')

while mais_termos != 0:
    while contador <= total_termos:
        print(f'{atual:.2f}', end=' -> ')
        atual += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
    total_termos += mais_termos

print('FIM')