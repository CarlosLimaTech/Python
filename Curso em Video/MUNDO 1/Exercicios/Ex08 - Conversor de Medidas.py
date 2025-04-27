print('='*60)
print('Conversor de M em CM e MM')
print('='*60)

medida = float(input('Digite a medida em metros (m): '))

centimetros = medida * 100
milimetros = medida * 1000

print('{} Metro(s) (m) \n{} Centimetros (cm) \n{} Milimetros (mm)'.format(medida, centimetros, milimetros))