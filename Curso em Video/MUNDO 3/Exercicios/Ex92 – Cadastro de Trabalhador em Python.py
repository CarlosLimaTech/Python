pessoa = dict()

# Entrada de dados
pessoa['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
pessoa['Idade'] = 2025 - ano_nascimento
pessoa['CTPS'] = int(input('N° Carteira de Trabalho (0 Caso não tenha): '))

if pessoa['CTPS'] != 0:
    pessoa['Ano_Contratacao'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Valor do salário R$: '))
    # Calculando o tempo de trabalho e idade de aposentadoria
    pessoa['Aposentadoria'] = (pessoa['Ano_Contratacao'] + 35) - ano_nascimento

# Exibindo os dados
print("\nDados cadastrados:")
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')