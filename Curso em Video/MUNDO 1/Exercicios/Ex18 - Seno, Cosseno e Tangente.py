from math import sin, cos, tan, radians

print('='*60)
print('Cosseno, Seno e Tangente'.center(60))
print('='*60)

angulo = float(input('Digite o angulo °: '))
angulo_radiano = radians(angulo)
seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
try:
    tangente = tan(angulo_radiano)
except:
    tangente = 'infinito'

print('Em relação ao Angulo {}°:'.format(angulo))
print('Seno = {:.2f}'.format(seno))
print('Cosseno = {:.2f}'.format(cosseno))
print('Tangente = ', tangente)