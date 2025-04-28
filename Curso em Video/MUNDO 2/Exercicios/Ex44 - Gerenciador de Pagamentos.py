print('='*60)
print('Gerenciador de Pagamentos'.center(60))
print('='*60)

valor_produto = float(input('Digite o valor do produto: '))

print('Escolha a forma de pagamento:')
print('[1] - A Vista (Dinheiro/Cheque) - Desconto de 10%')
print('[2] - A Vista (cartão) - Desconto de 5%')
print('[3] - 2 Vezes no Cartão - Sem Desconto')
print('[4] - 3 Vezes ou mais - 20% de Juros')
escolha = int(input('R: '))

if escolha == 1:
    valor_desconto = valor_produto - ((10/100) * valor_produto)
    print('Você escolheu a opção [{}] e o preço do produto será R${:.2f}'.format(escolha, valor_desconto))
elif escolha == 2:
    valor_desconto = valor_produto - ((5/100) * valor_produto)
    print('Você escolheu a opção [{}] e o preço do produto será R${:.2f}'.format(escolha, valor_desconto))
elif escolha == 3:
    print('Você escolheu a opção [{}] e o preço do produto será R${:.2f}'.format(escolha, valor_produto))
elif escolha == 4:
    valor_desconto = valor_produto + ((20/100) * valor_produto)
    print('Você escolheu a opção [{}] e o preço do produto será R${:.2f}'.format(escolha, valor_desconto))
else:
    print('Parece que você digitou {} e não é uma opção valida.... Tente novamente!'.format(escolha))    