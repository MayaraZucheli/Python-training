d = int(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar yma viagem de {d}Km.')
if d <= 200:
    preco = d * 0.50
    print(f'E o preço da sua passagem será de R${preco:.2f}')
else:
    preco = d * 0.45
    print(f'E o preço da sua passagem será de R${preco:.2f}')