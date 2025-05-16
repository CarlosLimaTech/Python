def mostrar_tela(mensagem):
    tamanho_linha = len(mensagem) + 2

    print('-' * tamanho_linha)
    print(f'{mensagem}'.center(tamanho_linha))
    print('-' * tamanho_linha)

mostrar_tela('Hello World')
mostrar_tela('Carlos Eduardo Vieira de Lima')
mostrar_tela('Oi')