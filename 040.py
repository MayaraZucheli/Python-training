n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print(f'A média entre {n1} e {n2} é {media:.2f}')

if media >= 5:
    print('Aprovado')
else:
    print('Reprovado')