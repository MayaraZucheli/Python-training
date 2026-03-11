t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' - ')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar mais: '))
print('FIM')