print('='*60)
print('Conversor de Bases Númericas'.center(60))
print('='*60)

valor = int(input('Digite um número: '))

print('Escolha para qual base converter esse número:')
base_escolhida = int(input('[1] Binário \n[2] Octal \n[3] Hexadecimal \n'))

if base_escolhida == 1:
    print('O número {} em Binário é equivalente á {}'.format(valor, bin(valor)[2:]))
elif base_escolhida == 2:
    print('O número {} em Octal é equivalente á {}'.format(valor, oct(valor)[2:]))
elif base_escolhida == 3:
    print('O número {} em Hexadecimal é equivalente á {}'.format(valor, hex(valor)[2:]))
else:
    print('Escolha invalida! Tente novamente...')    