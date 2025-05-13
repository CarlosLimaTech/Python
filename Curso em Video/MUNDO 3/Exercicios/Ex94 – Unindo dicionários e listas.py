dados_pessoa = dict()
lista_pessoas = list()

while True:
    dados_pessoa['Nome'] = str(input('\nNome: '))
    
    while True:
        sexo = str(input('Sexo [F/M]: ')).strip().upper()

        if sexo in ['M','F']:
            dados_pessoa['Sexo'] = sexo
            break
        else:
            print('Valor incorreto... Tente novamente')
    
    dados_pessoa['Idade'] = int(input('Idade: '))

    lista_pessoas.append(dados_pessoa.copy())

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    
    if continuar in 'N':
        break

print(f'\nA - {len(lista_pessoas)} foram cadastradas')

soma_idades = 0
lista_mulheres = list()
for indice, pessoa in enumerate(lista_pessoas):
    soma_idades += pessoa['Idade']

    if pessoa['Sexo'] in 'F':
        lista_mulheres.append(pessoa['Nome'])

media_idade = soma_idades/len(lista_pessoas)

print(f'B - Média das idades = {media_idade}')

print(f'C - Lista com as mulheres = {lista_mulheres}')

lista_pessoas_acima_media = list()

for indice, pessoa in enumerate(lista_pessoas):
    if pessoa['Idade'] > media_idade:
        lista_pessoas_acima_media.append(pessoa['Nome'])

print(f'D - Lista de pessoas com idade acima da média = {lista_pessoas_acima_media}')