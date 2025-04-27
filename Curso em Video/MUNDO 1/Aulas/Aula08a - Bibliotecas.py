import math #importa todas as funcionalidades da biblioteca
#from math import sqrt #importa funcionalidade especifica
#Para instalar bibliotecas python -m pip install {package_name}

num = int(input('Digite um número inteiro: '))
raiz = math.sqrt(num)

print('A raiz quadrada é {:.2f}'.format(raiz))
print('A raiz quadrada é {}'.format(math.ceil(raiz))) #arredonda para cima
print('A raiz quadrada é {}'.format(math.floor(raiz))) #arredonda para baixo