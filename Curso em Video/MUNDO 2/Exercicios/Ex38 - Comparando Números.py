print('='*60)
print('Alistamento Militar'.center(60))
print('='*60)

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 > numero2:
    print('O 1° número {} é maior que o 2° {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('O 2° número {} é maior que o 1° {}'.format(numero2, numero1))
elif numero1 == numero2:
    print('O 1° número {} é = ao 2° {}'.format(numero1, numero2)) 
else:
    print('Ocorreu um erro....')       