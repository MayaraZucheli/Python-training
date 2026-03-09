soma = 0

for count in range(1, 501, 2):
    if count % 3 == 0:
        soma += count
print(f'A soma de todos os números é {soma}')