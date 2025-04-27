import random

print('='*60)
print('Ordem de Apresentação'.center(60))
print('='*60)

alunos = []

for i in range(4):
    nome = str(input('Digite o nome do {}° aluno: '.format(i+1)))
    alunos.append(nome)

random.shuffle(alunos)

print('\nA ordem de apresentação sera: ')

for i in range(4):
    print('{}° {}'.format(i+1, alunos[i]))