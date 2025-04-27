print('='*60)
print('Conversor de R$ -> U$'.center(60))
print('='*60)

reais = float(input('Digite quantos R$ você possui: '))
dolar = reais / 3.27

print('Você possui R$ {} e pode comprar U$ {:.2f}'.format(reais, dolar))