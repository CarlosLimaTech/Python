print('='*60)
print('Aprovando Emprestimos'.center(60))
print('='*60)

valor_casa = float(input('Digite o valor da Casa R$'))
salario = float(input('Digite o valor do seu salário R$'))
anos_pagamento = int(input('Digite em quantos anos você planeja pagar a casa: '))
valor_parcela_mensal = valor_casa / (anos_pagamento * 12)
trinta_porcento_salario = ((30/100) * salario)

if valor_parcela_mensal > trinta_porcento_salario:
    print('\nSeu emprestismo foi negado!')
    print('O valor da parcela ficará R${:.2f} representando mais de 30% {:.2f} do seu salário!'.format(valor_parcela_mensal, trinta_porcento_salario))
elif valor_parcela_mensal < trinta_porcento_salario:
    print('\nSeu emprestismo foi Aprovado!')
    print('O valor da parcela ficará R${:.2f} representando menos de 30% ({:.2f}) do seu salário!'.format(valor_parcela_mensal, trinta_porcento_salario))
else:
    print('Impossivel Calcular!!')