from math import hypot

print('='*60)
print('Valor da Hipotenusa'.center(60))
print('='*60)

cateto_oposto = float(input('Digite o valor do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)

print('A hipotenusa é {:.2f}'.format(hipotenusa))