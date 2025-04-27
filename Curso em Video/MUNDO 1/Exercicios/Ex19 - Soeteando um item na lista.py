import random

print('='*60)
print('Sorteio de Alunos'.center(60))
print('='*60)

alunos = []

for i in range(4):
    nome = str(input('Digite o nome do {}° aluno: '.format(i+1)))
    alunos.append(nome)

sorteado = random.choice(alunos)

print('\nO aluno sorteado foi o {}!'.format(sorteado))