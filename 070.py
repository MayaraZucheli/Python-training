c = 0
total = 0
mil = 0
continuar = 'S'
menor_preco = 0
produto_barato = ''
while continuar == 'S':
    prod = input('Nome do produto: ')
    preco = float(input('Preço: '))
    continuar = input('Quer continuar? [S|N] ').upper()
    c += 1
    total += preco
    if preco > 1000:
        mil += 1
    if c == 1:
        menor_preco = preco
        produto_barato = prod
    else:
         if preco < menor_preco:
            menor_preco = preco
            produto_barato = prod
    if continuar == 'N':
        break
print(f'O total da compra foi de: {total:.2f}')
print(f'Temos {mil} produto custando mais de R$1000,00')
print(f'O produto mais barato foi a {produto_barato} que custa {menor_preco}')