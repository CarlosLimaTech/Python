print('='*60)
print('Pode ser um triangulo?'.center(60))
print('='*60)

lado1 = float(input('Digite o 1° lado: '))
lado2 = float(input('Digite o 2° lado: '))
lado3 = float(input('Digite o 3° lado: '))

if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado1 + lado3 > lado2:
    print('\nOs lados \n1 - {} \n2 - {} \n3 - {} \npodem fomar um trinagulo!'.format(lado1, lado2, lado3))
else:
    print('Os lados \n1 - {} \n2 - {} \n3 - {} \nNão podem fomar um trinagulo!'.format(lado1, lado2, lado3)) 