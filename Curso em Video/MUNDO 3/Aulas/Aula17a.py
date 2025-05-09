#Listas

valores = [2, 5, 9, 1, 2]
print(f'Lista - {valores}\n')

valores[2] = 3
print(f'Adicionando 3 na posição 2 - {valores}\n')

valores.append(7)
print(f'Adicionando 7 na lista - {valores}\n')

valores.insert(2, 0)
print(f'Inserindo 0 na posição 2 - {valores}\n')

valores.pop()
print(f'Eliminando elemento final da lista - {valores}\n')

valores.pop(2)
print(f'Eliminando número na posição 2 = {valores}\n')

valores.sort()
print(f'Ordenando do menor -> maior - {valores}\n')

valores.sort(reverse=True)
print(f'Ordenando do maior -> menor - {valores}\n')

print(f'Essa lista tem {len(valores)} elementos\n')

valores.remove(2)
print(f'Removendo a primeira ocorrência do número 2 - {valores}\n')

for contador, valor in enumerate(valores):
    print(f'Na posição {contador}, encontrei o valor {valor}!')
print('Cheguei ao fim...\n')

a = [2, 3, 4, 5]
#quando isso é feito, é criando um espelho. Então tudo que acontece em a reflete em b e viser versa
b = a
b[2] = 8
print(f'Lista {a}\n')
print(f'Lista {b}\n')

#jeito correto de fazer
a = [2, 3, 4, 5]
b = a[:]
b[2] = 8
print(f'Lista {a}\n')
print(f'Lista {b}\n')