aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input('Digite a média do aluno: '))

if aluno['Media'] <= 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'{k} é {v}')