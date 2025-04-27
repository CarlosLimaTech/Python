print('='*60)
print('Radar Eletrônico'.center(60))
print('='*60)

valor = int(input('Digite um número inteiro: '))

if valor % 2 == 0:
    print('O número {} é par!'.format(valor))
else: 
    print('O número {} é ímpar!'.format(valor))