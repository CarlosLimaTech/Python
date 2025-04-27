print('='*60)
print('Procurando uma string dentro de outra'.center(60))
print('='*60)

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))