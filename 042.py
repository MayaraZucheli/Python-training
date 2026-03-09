a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if (a + b > c) and (b + c > a) and (a + c > b):
    print('Essas 3 retas podem formar um triângulo ', end='')
    if a== b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print ('Com essas retas não temos um triângulo.')