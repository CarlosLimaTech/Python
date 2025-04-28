print('='*60)
print('IMC'.center(60))
print('='*60)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é = {:.2f}: Você está ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é = {:.2f}: Você está no PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é = {:.2f}: Você está em SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é = {:.2f}: Você está em OBESIDADE'.format(imc))
elif imc >= 40:
    print('Seu IMC é = {:.2f}: Você está OBESIDADE MÓRBIDA'.format(imc))
else:
    print('Parece que algo deu erraod :(')    