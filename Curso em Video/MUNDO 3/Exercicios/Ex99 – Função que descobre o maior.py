def maior(* num):
    if len(num) == 0:
        print('Nenhum valor informado.')
        return
    maior_valor = num[0]
    for valor in num:
        if valor > maior_valor:
            maior_valor = valor
    print(f'Você digitou {len(num)} valores e o maior é o {maior_valor}')

maior(4, 8, 9, 1, 7)
maior(85, 2, 7, 1001, 14)