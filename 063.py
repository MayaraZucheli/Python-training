print('Sequência de Fibonacci')
n = int(input('Quantos números vc quer mostrar? '))

a = 0
b = 1
contador = 0
while contador < n:
    c = a + b
    a = b
    b = c
    contador += 1
    print(a, end = ' - ')
print('FIM')