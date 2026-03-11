
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))

cont = 0

while cont < 10:
    termo = t + cont * r
    print(f'{termo}', end=' - ')
    cont += 1
print('FIM')