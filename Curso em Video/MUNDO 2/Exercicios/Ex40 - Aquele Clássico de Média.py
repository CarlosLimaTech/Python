print('='*60)
print('Média'.center(60))
print('='*60)

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média é de {} e ppor isso foi REPROVADO!'.format(media))
elif media > 5.0 and media < 6.9:
    print('Sua média é de {} e ppor isso esta de RECUPERAÇÃO!'.format(media))
elif media > 7.0:
    print('Sua média é de {} e ppor isso foi APROVADO!'.format(media))
else:
    print('Ocorreu um erro...')