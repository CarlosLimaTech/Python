print('='*60)
print('Quantidade de tinta necessária'.center(60))
print('='*60)

altura = float(input('Digite a Altura da parede em metros (m): '))
largura = float(input('Digite a largura da parede em metros (m): '))
area = largura * altura
litro_tinta = area / 2

print('\nA área é {:.2f}m²!'.format(area))
print('\nEntão você precisará de {:.2f}L de tinta.'.format(litro_tinta))