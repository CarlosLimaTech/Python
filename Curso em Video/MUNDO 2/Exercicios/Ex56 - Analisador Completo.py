print('=' * 60)
print('Analisador Completo'.center(60))
print('=' * 60)

soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f'\n----- {i}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / 4

print('\nRESULTADOS:')
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
if homem_mais_velho:
    print(f'O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo, há {mulheres_menos_20} mulher(es) com menos de 20 anos.')