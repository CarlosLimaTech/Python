valor = input('Digite alguma coisa: ')

print(f'Você digitou "{valor}" e essas são as informações dele:\n')

print('O tipo primitivo é:', type(valor))
print('É decimal?', valor.isdecimal())
print('É alfanumérico (letras e/ou números)?', valor.isalnum())
print('É numérico?', valor.isnumeric())
print('Tem só espaços?', valor.isspace())
print('Está no formato de título?', valor.istitle())
print('Está em maiúsculas?', valor.isupper())
