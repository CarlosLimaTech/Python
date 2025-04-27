print('='*60)
print('Separando digitos de números'.center(60))
print('='*60)

num = int(input('Digite um valor: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))