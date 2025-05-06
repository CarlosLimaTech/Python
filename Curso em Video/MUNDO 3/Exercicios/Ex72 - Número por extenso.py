numero_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
                  'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
                  'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
                  'Dezenove', 'Vinte')

while True:
    escolha = int(input('Digite um número entre 0 - 20: '))
    if 0 <= escolha <= 20:
        break
    print('Número inválido. Tente novamente.')

print(f'Você escolheu o número {escolha} que é escrito por extenso da forma "{numero_extenso[escolha]}"')