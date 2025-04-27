print('='*60)
print('Reajuste  Salarial'.center(60))
print('='*60)

salario = float(input('Digite seu salário R$ '))
salario_aumento = ((15 / 100) * salario) + salario

print('Salário com aumento de 15% = R$ {:.2f}'.format(salario_aumento))