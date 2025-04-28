print('='*60)
print('Criando um Menu de Opções'.center(60))
print('='*60)

menu = 4

while menu != 5:
    
    if menu == 1:
        print('A soma entre {} + {} = {}'.format(valor1, valor2, valor2 + valor1))
    elif menu == 2:
        print('A multiplicação entre {} X {} = {}'.format(valor1, valor2, valor2 * valor1))
    elif menu == 3:
        if valor1 > valor2:
            print('O Maior entre {} e {} é o {}'.format(valor1, valor2, valor1))
        elif valor2 > valor1:
            print('O Maior entre {} e {} é o {}'.format(valor1, valor2, valor2))
        else:
            print('Os valores {} e {} são iguais'.format(valor1, valor2))
    elif menu == 4:
        valor1 = float(input('Digite o 1° Valor: '))
        valor2 = float(input('Digite o 2° valor: '))
    else:
        print('Opção invalida, tente novamente!')
    
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Verificar o Maior')
    print('[4] - Novos Números')
    print('[5] - Sair')
    menu = int(input('oque você deseja fazer?'))

print('Saindo do Programa....')