times = (
    'Atlético Goianiense', 'Atlético Mineiro', 'Atlético Paranaense', 'Avaí',
    'Bahia', 'Botafogo', 'Chapecoense', 'Corinthians', 
    'Coritiba', 'Cruzeiro', 'Flamengo', 'Fluminense', 
    'Grêmio', 'Palmeiras', 'Ponte Preta', 'Santos', 
    'São Paulo', 'Sport', 'Vasco da Gama', 'Vitória'
)

print('A - Os 5 primeiros colocados são: ')
for i in range(5):
    print(f'{i+1}° {times[i]}')

print('\nB - Os últimos 4 colocados são:')
for i in range(-4, 0):
    print(f'{len(times) + i + 1}° {times[i]}')

time_procurado = 'Chapecoense'
if time_procurado in times:
    posicao = times.index(time_procurado) + 1
    print(f'\n{time_procurado} está na {posicao}ª posição.')
else:
    print(f'{time_procurado} não está na lista de times.')