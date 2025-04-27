print('='*60)
print('Primeira e última ocorrência em uma string'.center(60))
print('='*60)

n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu 1° nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))