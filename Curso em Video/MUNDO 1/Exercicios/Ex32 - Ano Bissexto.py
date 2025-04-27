print('='*60)
print('Ano Bissexto'.center(60))
print('='*60)

year = int(input("Digite um ano para verificar se é bissexto: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"O ano {year} é bissexto.")
else:
    print(f"O ano {year} não é bissexto.")