
v1 = 1
v2 = 1
while v1 and v2 != 0:
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite um valor: '))
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    op = int(input('Qual a sua opção? '))
    if op == 1:
        print(f'O resultado de {v1} + {v2} é {v1 + v2}')
    elif op == 2:
        print(f'O resultado de {v1} X {v2} é {v1 * v2}')
    elif op == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior é {v1}')
        else:
            print(f'Entre {v1} e {v2} o maior é {v2}')
    elif op == 4:
        print('Insira novos números')
    else:
        break
print('Tchau!')