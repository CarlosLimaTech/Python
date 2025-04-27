print('='*60)
print('Aluguel de Carros'.center(60))
print('='*60)

dias_alugado = int(input('Digite a quantidade de dias alugado: '))
km_rodados = float(input('Digite a quantidade de KM percorridos: '))

valor_dias = (dias_alugado * 60)
valor_km = (km_rodados * 0.15)
valor_total = valor_dias + valor_km

print('O valor a pagar pelo aluguel R${:.2f} e pelos KM percorridos é R${:.2f} totalizando R${:.2f}'.format(valor_dias, valor_km, valor_total))