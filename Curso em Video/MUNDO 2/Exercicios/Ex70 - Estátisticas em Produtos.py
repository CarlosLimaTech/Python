print('=' * 60)
print('Estatísticas em Produtos'.center(60))
print('=' * 60)

total_gasto = 0
produtos_mais_de_1000 = 0
produto_mais_barato = ''
preco_mais_barato = None

while True:
    nome_produto = input('Digite o nome do produto: ').strip()
  
    while True:
        try:
            preco_produto = float(input('Digite o preço do produto: R$ '))
            if preco_produto < 0:
                print('O preço não pode ser negativo. Tente novamente.')
            else:
                break
        except ValueError:
            print('Por favor, digite um valor numérico válido para o preço.')

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_de_1000 += 1

    if preco_mais_barato is None or preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite "S" para continuar ou "N" para sair.')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print('\nFim do programa. Aqui estão os resultados:')
print(f'A) O total gasto na compra foi R$ {total_gasto:.2f}.')
print(f'B) {produtos_mais_de_1000} produto(s) custam mais de R$1000.00.')
print(f'C) O produto mais barato foi "{produto_mais_barato}" que custa R$ {preco_mais_barato:.2f}.')