c = 'S'
cont = 0
cont_m = 0
cont_f = 0
while c == 'S':
    print('Cadastre uma pessoa')
    print('-------------------')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M|F]: ').upper()
    print('-------------------')
    c = input('Quer continuar? [S|N] ').upper()
    
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1
    if c == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {cont_m} homens cadastrados')
print(f'E temos {cont_f} mulher com menos de 20 anos')
