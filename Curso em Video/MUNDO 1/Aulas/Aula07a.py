#Alinhado objetos dentro de um print

#nome = input('Digite alguma coisa: ')
#print('{:^20}'.format(nome)) #Centralizado em XAna espaços
#print('{:<20}'.format(nome)) #Alinhado a esquerda em X espaços
#print('{:>20}'.format(nome)) #Alinhado a direita em X espaços
#print('{:=^20}'.format(nome)) #Alinhado colocando coisas nos espaços em branco

N1 = int(input('Digite um valor: '))
N2 = int(input('Digite outro valor: '))
soma = N1 + N2
multiplicacao = N1 * N2
divisao = N1 / N2
divisao_inteira = N1 // N2
divisao_resto = N1 % N2
potencia = N1 ** N2

print('='*50)
print('Realizando opreações matemáticas com {} e {}'.format(N1, N2))
print('='*50)
print('\n') #Pula uma linha
print('A soma é {}'.format(soma), end = ' ') #Permite que o print fique na mesma linha
print('A multiplicação é {}'.format(multiplicacao))
print('A divisão é {:.2f}'.format(divisao))
print('A divisão inteira é {}'.format(divisao_inteira))
print('O resto da divisão é {}'.format(divisao_resto))
print('A potencia é {}'.format(potencia))