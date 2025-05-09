print('='*40)
print(f'{"Dividindo valores em várias listas":^40}')
print('='*40)

expressao = str(input('Digite a expressão matemática: '))

numero_parenteses_lado1 = numero_parenteses_lado2 = 0

for pos in range (len(expressao)):
    if'(' in expressao[pos]:
        numero_parenteses_lado1 += 1

    if')' in expressao[pos]:
        numero_parenteses_lado2 += 1

if numero_parenteses_lado1 == numero_parenteses_lado2:
    print('A expressão é valida!')
else:
    print('A expressão Não é valida!')