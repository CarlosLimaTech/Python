#Nome = str(input('Qual é o seu nome? '))
#if Nome == 'Gustavo':
#    print('Que nome bonito!')
#else:
#    print('Seu nome é tão normal!')   
#print('Bom dia, {}!'.format(Nome))

n1 = int(input('Digite a 1 nota: '))
n2 = int(input('Digite a 2 nota: '))
m = (n1 + n2) / 2
print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#Fazendo o mesmo código, mas com o if e else em uma linha só
# print('Sua média foi boa! PARABÉNS!' if m >= 6 else 'Sua média foi ruim! ESTUDE MAIS!')