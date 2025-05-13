""" pessoas = {
    'nome':'Gustavo',
    'sexo':'M',
    'idade':22
}

pessoas['peso'] = 98.5

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) """

brasil = list()
estado = dict()

for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
print(brasil)