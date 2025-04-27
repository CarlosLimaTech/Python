import math

print('='*60)
print('Quebrando Números'.center(60))
print('='*60)

valor = float(input('Digite um número: '))
inteiro = math.trunc(valor)
resto = valor - inteiro

print('Valor digitado {}, valor inteiro {}, valor fracionário {:.2f}'.format(valor, inteiro, resto))