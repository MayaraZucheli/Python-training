

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
       print('Programa encerrado')
       break

    cont = 1
    while cont <= 10:
        print (f'{n} X {cont} = {n * cont}')
        cont += 1