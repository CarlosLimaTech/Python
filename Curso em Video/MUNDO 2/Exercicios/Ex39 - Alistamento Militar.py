print('='*60)
print('Alista Militar'.center(60))
print('='*60)

ano_nascimento = int(input('Informe o seu ano de nascimento: '))
idade = 2025 - ano_nascimento

if idade < 18:
    print('Você não está na idade de se alistar, faltam {} ano(s)!'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar!')
elif idade > 18:
    print('Você já passou da hora de se alistar, passando {} ano(s)!'.format(idade - 18))
else:
    print('Ocorreu um erro!')    