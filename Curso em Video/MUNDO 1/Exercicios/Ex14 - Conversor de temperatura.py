print('='*60)
print('Conversor de Temperatura'.center(60))
print('='*60)

celsius = float(input('Digite a temperatura (°C): '))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print('{}°C é equivalente a {:.2f}°F e {:.2f}°K'.format(celsius, fahrenheit, kelvin))