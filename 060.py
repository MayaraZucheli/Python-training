n = int(input('Digite um número para calcular seu fatorial: '))
fat = 1

print(f'Calculando {n}! = ', end='')

contador = n
while contador > 0:
    print(contador, end=' ')
    print('x ' if contador > 1 else '= ', end='')
    fat *= contador
    contador -= 1

print(fat)