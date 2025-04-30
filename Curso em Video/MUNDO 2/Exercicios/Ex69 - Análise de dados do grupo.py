print('=' * 60)
print('Análise de Dados do Grupo'.center(60))
print('=' * 60)

contador_pessoas_mais18anos = 0
contador_homens = 0
contador_mulheres_menos20anos = 0

while True:
    while True:
        try:
            idade = int(input('Digite a idade da pessoa: '))
            if idade < 0:
                print('A idade não pode ser negativa. Tente novamente.')
            else:
                break
        except ValueError:
            print('Por favor, digite um número inteiro válido para a idade.')

    while True:
        sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print('Opção inválida! Digite "M" para masculino ou "F" para feminino.')

    if idade >= 18:
        contador_pessoas_mais18anos += 1

    if sexo == 'M':
        contador_homens += 1
    elif sexo == 'F' and idade < 20:
        contador_mulheres_menos20anos += 1

    while True:
        escolha = input('Deseja continuar? [S/N]: ').strip().upper()
        if escolha in ['S', 'N']:
            break
        else:
            print('Opção inválida! Digite "S" para continuar ou "N" para sair.')

    if escolha == 'N':
        break

print('\nFim do Programa e foram encontrados...')
print(f'A - {contador_pessoas_mais18anos} pessoa(s) com mais de 18 anos.')
print(f'B - {contador_homens} homem(ns) cadastrados.')
print(f'C - {contador_mulheres_menos20anos} mulher(es) com menos de 20 anos.')