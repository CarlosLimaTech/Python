print('='*60)
print('Custo de Viagem'.center(60))
print('='*60)

km_viagem = float(input('Digite a distância da viagem em KM: '))

if km_viagem <= 200:
    custo  = km_viagem * 0.50
    print('O valor da viagem é de R${:.2f}'.format(custo))
else:
    custo = km_viagem * 0.45
    print('O custo da viagem é de R${}'.format(custo))    