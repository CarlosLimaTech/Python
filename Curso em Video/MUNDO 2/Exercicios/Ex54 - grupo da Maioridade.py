from datetime import date

print('=' * 60)
print('Grupo da Maioridade'.center(60))
print('=' * 60)

ano_atual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\nNo total, {maiores} pessoa(s) já atingiram a maioridade.')
print(f'E {menores} pessoa(s) ainda não atingiram a maioridade.')