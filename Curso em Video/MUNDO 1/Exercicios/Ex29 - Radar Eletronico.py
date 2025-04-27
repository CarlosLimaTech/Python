print('='*60)
print('Radar Eletrônico'.center(60))
print('='*60)

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Você está acima da vlocidade e por isso foi multado!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar R${:.2f} de multa!'.format(multa))
else:
    print('Você está conforme a velocidade permitidade. Pode continuar!')
print('Tenha um bom dia! Dirija com segurança!')