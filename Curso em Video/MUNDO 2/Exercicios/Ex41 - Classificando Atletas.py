print('='*60)
print('Classificando Atletas'.center(60))
print('='*60)

ano_nacimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual - ano_nacimento

if idade > 0 and idade <= 9:
    print('Idade = {} - Classificação = MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Idade = {} - Classificação = INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Idade = {} - Classificação = JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Idade = {} - Classificação = SENIOR'.format(idade))
elif idade > 20:
    print('Idade = {} - Classificação = MASTER'.format(idade))
else:
    print('Ocorreu um erro.... Você digitou {} no ano de nascimento, e {} no ano atual!'.format(ano_nacimento, ano_atual))    