soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher = 0
for i in range(1, 4):
    print(f'----- {i} Pessoa -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M|F]: ').strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if i == 1 and sexo in 'Ff' and idade < 20:
        mulher += 1

media_idade = soma_idade / 3
print(f'A média de idade do grupo é de {media_idade:.2f} anos')
print(f'O homem mais velho é {nome_velho} e ele tem {maior_idade_homem} anos')
print(f'{mulher} Mulher tem menos de 20 anos anos')
