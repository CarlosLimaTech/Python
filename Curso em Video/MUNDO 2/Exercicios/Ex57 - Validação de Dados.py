print('=' * 60)
print('Validação de Dados'.center(60))
print('=' * 60)

sexo = ''
while sexo not in ['M', 'F']:
    sexo = input('Digite o seu sexo [M/F]: ').strip().upper()
    if sexo not in ['M', 'F']:
        print('Você digitou um valor inválido. Tente novamente!')

print(f'Sexo {sexo} registrado com sucesso!')