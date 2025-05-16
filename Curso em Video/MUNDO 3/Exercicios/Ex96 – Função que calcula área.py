def calcular_area(largura, altura):
    area = largura * altura
    print(f'A área de um terreno {largura}X{altura} é de {area}m²')

largura = float(input('Largura: '))
altura = float(input('Altura: '))

calcular_area(largura, altura)