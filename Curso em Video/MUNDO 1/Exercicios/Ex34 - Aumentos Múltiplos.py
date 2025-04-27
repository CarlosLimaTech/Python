print('='*60)
print('Aumentos Múltiplos'.center(60))
print('='*60)

salario = float(input('Digite o valor do seu salário R$'))

if salario > 1250:
    novo_salario = 1250 + (10/100 * salario)
else:
    novo_salario = 1250 + (15/100 * salario)

print('Seu novo salário é de R${:.2f}'.format(novo_salario))        