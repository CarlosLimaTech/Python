print('='*60)
print('Analisando Triângulos V2.0'.center(60))
print('='*60)

lado1 = float(input('Digite o 1° lado: '))
lado2 = float(input('Digite o 2° lado: '))
lado3 = float(input('Digite o 3° lado: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print(f'\nOs lados \n1 - {lado1} \n2 - {lado2} \n3 - {lado3} \nPodem formar um triângulo!')
    if lado1 == lado2 == lado3:
        print('\nO triângulo será Equilátero!')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('\nO triângulo será Isósceles!')
    else:
        print('\nO triângulo será Escaleno!')
else:
    print(f'Os lados \n1 - {lado1} \n2 - {lado2} \n3 - {lado3} \nNão podem formar um triângulo!')