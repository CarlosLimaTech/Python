print('='*60)
print('Calculo de Desconto'.center(60))
print('='*60)

valor_total = float(input('Digite o valor total: '))
porcentagem = float(input('Digite a porcentagem: '))

resultado = valor_total - ((valor_total * porcentagem) / 100)

print('Resultado: {:.2f}'.format(resultado))
