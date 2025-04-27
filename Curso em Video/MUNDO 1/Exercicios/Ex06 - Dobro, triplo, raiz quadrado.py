import math

print('='*60)
print('Dobro, Triplo e Raiz Quadrada')
print('='*60)

valor = int(input('Digite um valor: '))

dobro = valor * 2
triplo = valor * 3
raiz_quadrada = math.sqrt(valor)
raiz_quadrada2 = valor ** (1/2)

print('O valor digitado foi {}'.format(valor))
print('O Dobro é {}'.format(dobro))
print('O Triplo é {}'.format(triplo))
print('A Raiz quadrada é {}'.format(raiz_quadrada))
print('A Raiz quadrada2 é {}'.format(raiz_quadrada2))