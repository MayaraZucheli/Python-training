lista = []

for i in range(1,4):
    peso = float(input(f'Peso da {i} pessoa? '))
    lista += [peso]

print(f'o maior peso lido foi {max(lista)}')
print(f'o menor peso lido foi {min(lista)}')
