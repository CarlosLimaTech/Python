print('=' * 60)
print('Tabuada V2.0'.center(60))
print('=' * 60)

valor = int(input('Digite um número inteiro: '))

print('='*60)
print('Tabuada do {}'.format(valor).center(60))
print('='*60)

for i in range (11):
    print('{:2} X {:2} = {}'.format(valor, i, valor * i))