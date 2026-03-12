c = str('S').upper()
cont = 0
soma = 0
lista = []
while c == 'S':
    cont += 1
    n = int(input('Digite um número: '))
    soma += n
    media = soma / cont
    c = input('Quer continuar? [S/N] ').upper()
    lista.append(n)
print(f'Você digitou {cont} e a média entre esses números é {media}')
print(f'o maior valor foi de {max(lista)} e o menor foi de {min(lista)}')